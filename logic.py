import sqlite3
from config import DEPARTMENTS, FAQ

class SupportDB:
    def __init__(self):
        self.conn = sqlite3.connect('support.db')
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                username TEXT,
                department TEXT,
                problem TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def add_ticket(self, user_id, username, department, problem):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO tickets (user_id, username, department, problem)
            VALUES (?, ?, ?, ?)
        ''', (user_id, username, department, problem))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_user_tickets(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, department, problem, created_at FROM tickets WHERE user_id = ? ORDER BY id DESC', (user_id,))
        return cursor.fetchall()
    
    def delete_ticket(self, ticket_id, user_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM tickets WHERE id = ? AND user_id = ?', (ticket_id, user_id))
        self.conn.commit()
        return cursor.rowcount > 0

class FAQProcessor:
    def get_answer(self, text):
        text = text.lower()
        for key, data in FAQ.items():
            if key in text:
                return data['answer']
        return None
    
    def get_faq_list(self):
        return "\n".join([f"• {data['question']}" for data in FAQ.values()])