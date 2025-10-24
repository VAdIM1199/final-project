from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler
from logic import SupportDB, FAQProcessor
from config import TOKEN, DEPARTMENTS

db = SupportDB()
faq = FAQProcessor()
user_data = {}

def main_menu():
    return ReplyKeyboardMarkup([
        [' FAQ', 'Заявка'],
        [' Мои заявки', 'Помощь']
    ], resize_keyboard=True)

def departments_menu():
    return ReplyKeyboardMarkup([
        [DEPARTMENTS['programmers'], DEPARTMENTS['sales']],
        ['Назад']
    ], resize_keyboard=True)

def tickets_menu():
    return ReplyKeyboardMarkup([
        ['Удалить заявку', 'Назад']
    ], resize_keyboard=True)

async def start(update, context):
    await update.message.reply_text(
        "Бот поддержки магазина 'Продаем все на свете'\n\nВыберите действие:",
        reply_markup=main_menu()
    )

async def help_command(update, context):
    await update.message.reply_text(
        "Помощь:\n\n"
        "• FAQ - частые вопросы\n"
        "• Заявка - создать заявку\n"
        "• Мои заявки - история обращений\n\n"
        "Контакты: +7 (495) 123-45-67",
        reply_markup=main_menu()
    )

async def show_faq(update, context):
    await update.message.reply_text(
        f" Частые вопросы:\n\n{faq.get_faq_list()}",
        reply_markup=main_menu()
    )

async def create_ticket(update, context):
    user_id = update.message.from_user.id
    user_data[user_id] = {'state': 'choose_department'}
    await update.message.reply_text("Выберите отдел:", reply_markup=departments_menu())

async def show_tickets(update, context):
    user_id = update.message.from_user.id
    tickets = db.get_user_tickets(user_id)
    
    if not tickets:
        await update.message.reply_text(" У вас нет заявок", reply_markup=main_menu())
        return
    
    text = "Ваши заявки:\n\n"
    for ticket in tickets:
        dept = DEPARTMENTS.get(ticket[1], ticket[1])
        text += f"#{ticket[0]} - {dept}\n{ticket[2][:50]}...\n\n"
    
    await update.message.reply_text(text, reply_markup=tickets_menu())

async def delete_ticket_start(update, context):
    user_id = update.message.from_user.id
    tickets = db.get_user_tickets(user_id)
    
    if not tickets:
        await update.message.reply_text(" У вас нет заявок для удаления", reply_markup=main_menu())
        return
    
    user_data[user_id] = {'state': 'delete_ticket', 'tickets': tickets}
    
    text = "Ваши заявки (укажите номер для удаления):\n\n"
    for ticket in tickets:
        dept = DEPARTMENTS.get(ticket[1], ticket[1])
        text += f"#{ticket[0]} - {dept}\n{ticket[2][:50]}...\n\n"
    
    await update.message.reply_text(text, reply_markup=ReplyKeyboardRemove())

async def delete_ticket_finish(update, context):
    user_id = update.message.from_user.id
    text = update.message.text.strip()
    
    if not text.isdigit():
        await update.message.reply_text("Пожалуйста, введите номер заявки (только цифры)", reply_markup=tickets_menu())
        return
    
    ticket_id = int(text)
    user_tickets = user_data.get(user_id, {}).get('tickets', [])
    ticket_exists = any(ticket[0] == ticket_id for ticket in user_tickets)
    
    if not ticket_exists:
        await update.message.reply_text("Заявка с таким номером не найдена или не принадлежит вам", reply_markup=tickets_menu())
        return

    success = db.delete_ticket(ticket_id, user_id)
    
    if success:
        await update.message.reply_text(f"Заявка #{ticket_id} успешно удалена", reply_markup=main_menu())
    else:
        await update.message.reply_text("Ошибка при удалении заявки", reply_markup=main_menu())
    
    user_data.pop(user_id, None)

async def handle_message(update, context):
    text = update.message.text
    user_id = update.message.from_user.id

    if text == 'FAQ':
        await show_faq(update, context)
        return
    elif text == 'Заявка':
        await create_ticket(update, context)
        return
    elif text == 'Мои заявки':
        await show_tickets(update, context)
        return
    elif text == 'Помощь':
        await help_command(update, context)
        return
    elif text == 'Назад':
        user_data.pop(user_id, None)
        await start(update, context)
        return
    elif text == 'Удалить заявку':
        await delete_ticket_start(update, context)
        return
    
    state = user_data.get(user_id, {}).get('state')
    
    if state == 'choose_department':
        if text in [DEPARTMENTS['programmers'], DEPARTMENTS['sales']]:
            department = 'programmers' if text == DEPARTMENTS['programmers'] else 'sales'
            user_data[user_id] = {'state': 'describe_problem', 'department': department}
            dept_name = "Программисты" if department == 'programmers' else "Отдел продаж"
            await update.message.reply_text(f" {dept_name}\n Опишите проблему:")
        else:
            await update.message.reply_text("Выберите отдел из кнопок", reply_markup=departments_menu())
    
    elif state == 'describe_problem':
        department = user_data[user_id].get('department')
        ticket_id = db.add_ticket(user_id, update.message.from_user.username, department, text)
        dept_name = DEPARTMENTS[department]
        await update.message.reply_text(f"Заявка #{ticket_id} создана!\nОтдел: {dept_name}", reply_markup=main_menu())
        user_data.pop(user_id, None)
    
    elif state == 'delete_ticket':
        await delete_ticket_finish(update, context)
    
    else:
        answer = faq.get_answer(text)
        if answer:
            await update.message.reply_text(f" {answer}", reply_markup=main_menu())
        else:
            await update.message.reply_text(" Не нашел ответа. Создайте заявку ", reply_markup=main_menu())

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("my_tickets", show_tickets))
    app.add_handler(MessageHandler(None, handle_message))
    app.run_polling()

if __name__ == '__main__':
    main()