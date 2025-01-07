from models import Account, Database, Transaction

class Bank:
    def __init__(self):
        self.db = Database()
        
    def get_all_accounts(self):
        cursor = self.db.conn.cursor()
        return Account.find_all(cursor)
    
    def create_account(self, holder_name, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        cursor = self.db.conn.cursor()
        account = Account.create(cursor, holder_name, initial_balance)
        self.db.conn.commit()
        return account.account_number
    
    def close_account(self, account_number):
        cursor = self.db.conn.cursor()
        account = Account.find_by_account_number(cursor, account_number)
        if not account:
            raise ValueError("Account not found or inactive")
        if account.balance > 0:
            raise ValueError("Account has a balance, cannot be closed")
        account.close(cursor)
        self.db.conn.commit()
    
    def deposit(self, account_number, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        cursor = self.db.conn.cursor()
        
        account = Account.find_by_account_number(cursor, account_number)
        if not account:
            raise ValueError("Account not found or inactive")
        
        account.change_balance(cursor, amount)
        Transaction.create(cursor, account_number, 'deposit', amount)
        self.db.conn.commit()
    
    def withdraw(self, account_number, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        cursor = self.db.conn.cursor()
        account = Account.find_by_account_number(cursor, account_number)
        if not account:
            raise ValueError("Account not found or inactive")
        
        account.change_balance(cursor, -amount)
        Transaction.create(cursor, account_number, 'withdrawal', -amount)
        self.db.conn.commit()
    
    def transfer(self, from_account, to_account, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        cursor = self.db.conn.cursor()
        from_acc = Account.find_by_account_number(cursor, from_account)
        if not from_acc:
            raise ValueError("Source account not found or inactive")
        
        if from_acc.balance < amount:
            raise ValueError("Insufficient funds")
        
        to_acc = Account.find_by_account_number(cursor, to_account)
        if not to_acc:
            raise ValueError("Destination account not found or inactive")
        
        from_acc.change_balance(cursor, -amount)
        to_acc.change_balance(cursor, amount)
        
        Transaction.create(cursor, from_acc.account_number, 'transfer', -amount, to_acc.account_number)
        Transaction.create(cursor, to_acc.account_number, 'transfer', amount, from_acc.account_number)
        self.db.conn.commit()
    
    def get_balance(self, account_number):
        cursor = self.db.conn.cursor()
        account = Account.find_by_account_number(cursor, account_number)
        if not account:
            raise ValueError("Account not found or inactive")
        return account.balance
    
    def get_transactions(self, account_number):
        cursor = self.db.conn.cursor()
        account = Account.find_by_account_number(cursor, account_number)
        if not account:
            raise ValueError("Account not found or inactive")
        return Transaction.get_transactions(cursor, account_number)