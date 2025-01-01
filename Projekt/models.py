from datetime import datetime
import random
import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('bank.db')
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_number TEXT PRIMARY KEY,
                holder_name TEXT NOT NULL,
                balance REAL NOT NULL,
                created_at TIMESTAMP,
                status TEXT DEFAULT 'active'
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_number TEXT,
                transaction_type TEXT,
                amount REAL,
                timestamp TIMESTAMP,
                related_account TEXT NULL,
                FOREIGN KEY (account_number) REFERENCES accounts (account_number)
            )
        ''')
        self.conn.commit()

class Account:
    def __init__(self, account_number, holder_name, balance=0, status='active'):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance 
        self.status = status
        
    @staticmethod
    def create(cursor, holder_name, initial_balance=0):
        account_number = Account._generate_account_number()
        cursor.execute(
            "INSERT INTO accounts (account_number, holder_name, balance, created_at) VALUES (?, ?, ?, ?)",
            (account_number, holder_name, initial_balance, datetime.now())
        )
        return Account(account_number, holder_name, initial_balance)

    @staticmethod
    def find_by_account_number(cursor, account_number):
        cursor.execute(
            '''SELECT account_number, holder_name, balance, status 
            FROM accounts 
            WHERE account_number = ? AND status = 'active'
            ''',
            (account_number,)
        )
        result = cursor.fetchone()
        if result:
            return Account(result[0], result[1], result[2])
        return None

    @staticmethod
    def find_all(cursor):
        cursor.execute("SELECT account_number, holder_name, balance, status FROM accounts")
        accounts = []
        for row in cursor.fetchall():
            accounts.append(Account(row[0], row[1], row[2], row[3]))
        return accounts

    @staticmethod
    def _generate_account_number():
        return f"ACC{random.randint(10000, 99999)}" 
    
    def change_balance(self, cursor, amount):
        self.balance += amount
        cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE account_number = ?",
            (amount, self.account_number)
        )
        
    def close(self, cursor):
        cursor.execute(
            "UPDATE accounts SET status = 'closed' WHERE account_number = ?",
            (self.account_number,)
        )
        
        
class Transaction:
    def __init__(self, account_number, transaction_type, amount, timestamp, related_account=None):
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = timestamp
        self.related_account = related_account

    @staticmethod
    def create(cursor, account_number, transaction_type, amount, related_account=None):
        timestamp = datetime.now()
        cursor.execute(
            '''INSERT INTO transactions (account_number, transaction_type, amount, timestamp, related_account) 
            VALUES (?, ?, ?, ?, ?)''',
            (account_number, transaction_type, amount, timestamp, related_account)
        )
        return Transaction(account_number, transaction_type, amount, timestamp, related_account)

    @staticmethod
    def get_transactions(cursor, account_number):
        cursor.execute(
            '''SELECT account_number, transaction_type, amount, timestamp, related_account 
            FROM transactions 
            WHERE account_number = ? 
            ORDER BY timestamp DESC''',
            (account_number,)
        )
        transactions = []
        for row in cursor.fetchall():
            transactions.append(Transaction(row[0], row[1], row[2], row[3], row[4]))
        return transactions
