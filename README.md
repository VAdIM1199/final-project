<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Бот поддержки - Продаем все на свете</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
            padding: 40px 20px;
        }

        .header h1 {
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .header .subtitle {
            font-size: 1.4em;
            opacity: 0.9;
        }

        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }

        .card {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        }

        .card h2 {
            color: #4a5568;
            margin-bottom: 20px;
            font-size: 1.5em;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .card ul {
            list-style: none;
            padding-left: 0;
        }

        .card li {
            padding: 8px 0;
            border-bottom: 1px solid #e2e8f0;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .card li:last-child {
            border-bottom: none;
        }

        .feature-list li::before {
            content: "✅";
            font-size: 1.1em;
        }

        .command-list li::before {
            content: "⚡";
            font-size: 1.1em;
        }

        .database-list li::before {
            content: "📊";
            font-size: 1.1em;
        }

        .stats-list li::before {
            content: "📈";
            font-size: 1.1em;
        }

        .setup-steps {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 40px;
        }

        .setup-steps h2 {
            color: #4a5568;
            margin-bottom: 25px;
            font-size: 1.8em;
            text-align: center;
        }

        .step {
            display: flex;
            align-items: flex-start;
            gap: 20px;
            margin-bottom: 25px;
            padding: 20px;
            background: #f7fafc;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }

        .step-number {
            background: #667eea;
            color: white;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            flex-shrink: 0;
        }

        .step-content h3 {
            color: #4a5568;
            margin-bottom: 10px;
        }

        .code-block {
            background: #2d3748;
            color: #e2e8f0;
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
            font-family: 'Courier New', monospace;
            overflow-x: auto;
        }

        .departments {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 20px;
        }

        .department {
            background: #f7fafc;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }

        .department.programmers {
            border-top: 4px solid #4299e1;
        }

        .department.sales {
            border-top: 4px solid #48bb78;
        }

        .footer {
            text-align: center;
            color: white;
            padding: 30px;
            margin-top: 40px;
            font-size: 1.2em;
        }

        @media (max-width: 768px) {
            .card-grid {
                grid-template-columns: 1fr;
            }
            
            .departments {
                grid-template-columns: 1fr;
            }
            
            .header h1 {
                font-size: 2em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 Бот поддержки</h1>
            <div class="subtitle">для интернет-магазина "Продаем все на свете"</div>
        </div>

        <div class="card-grid">
            <div class="card">
                <h2>🎯 Что делает бот</h2>
                <ul class="feature-list">
                    <li>Автоответы на частые вопросы (20+ готовых ответов)</li>
                    <li>Создает заявки в 2 отдела</li>
                    <li>Сохраняет все обращения в базу данных</li>
                    <li>Удобное меню с кнопками</li>
                    <li>Круглосуточная поддержка</li>
                </ul>
            </div>

            <div class="card">
                <h2>⚡ Команды бота</h2>
                <ul class="command-list">
                    <li><strong>/start</strong> - главное меню</li>
                    <li><strong>/help</strong> - помощь и инструкции</li>
                    <li><strong>/ticket</strong> - создать новую заявку</li>
                    <li><strong>/faq</strong> - частые вопросы</li>
                    <li><strong>/status</strong> - статус моих заявок</li>
                </ul>
            </div>

            <div class="card">
                <h2>📊 База данных</h2>
                <ul class="database-list">
                    <li><strong>tickets</strong> - все заявки</li>
                    <li><strong>users</strong> - информация о клиентах</li>
                    <li><strong>departments</strong> - статистика отделов</li>
                    <li><strong>faq_usage</strong> - использование автоответов</li>
                </ul>
            </div>

            <div class="card">
                <h2>📈 Что отслеживаем</h2>
                <ul class="stats-list">
                    <li>Нагрузка по отделам</li>
                    <li>Время решения задач</li>
                    <li>Эффективность автоответов</li>
                    <li>Статистика обращений</li>
                    <li>Удовлетворенность клиентов</li>
                </ul>
            </div>
        </div>

        <div class="setup-steps">
            <h2>🚀 Быстрый старт</h2>
            
            <div class="step">
                <div class="step-number">1</div>
                <div class="step-content">
                    <h3>Установка зависимостей</h3>
                    <div class="code-block">pip install python-telegram-bot sqlite3</div>
                </div>
            </div>

            <div class="step">
                <div class="step-number">2</div>
                <div class="step-content">
                    <h3>Настройка бота</h3>
                    <p>Создайте бота через @BotFather в Telegram и получите токен</p>
                    <div class="code-block">BOT_TOKEN = "ваш_токен_здесь"</div>
                </div>
            </div>

            <div class="step">
                <div class="step-number">3</div>
                <div class="step-content">
                    <h3>Запуск бота</h3>
                    <div class="code-block">python bot.py</div>
                    <p>Бот готов к работе!</p>
                </div>
            </div>
        </div>

        <div class="card">
            <h2>👥 Отделы поддержки</h2>
            <div class="departments">
                <div class="department programmers">
                    <h3>👨‍💻 Программисты</h3>
                    <p><strong>Решают проблемы:</strong></p>
                    <ul>
                        <li>Ошибки сайта</li>
                        <li>Проблемы с оплатой</li>
                        <li>Технические сбои</li>
                        <li>Баги и ошибки</li>
                    </ul>
                </div>
                <div class="department sales">
                    <h3>👨‍💼 Отдел продаж</h3>
                    <p><strong>Решают проблемы:</strong></p>
                    <ul>
                        <li>Вопросы о товарах</li>
                        <li>Проблемы с доставкой</li>
                        <li>Возвраты и обмены</li>
                        <li>Консультации</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="footer">
            <p>🚀 <strong>Готов к работе!</strong> Запускайте и экономьте время поддержки 🎯</p>
        </div>
    </div>

    <script>
        // Анимация появления карточек
        document.addEventListener('DOMContentLoaded', function() {
            const cards = document.querySelectorAll('.card');
            cards.forEach((card, index) => {
                setTimeout(() => {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    card.style.transition = 'all 0.6s ease';
                    
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 100);
                }, index * 200);
            });
        });
    </script>
</body>
</html>
