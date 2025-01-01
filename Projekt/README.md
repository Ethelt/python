# Bank Management System

A simple command-line banking application that allows bank employees to manage customer accounts, handle transactions, and maintain records in an SQLite database.

## Features

- Create and close bank accounts
- Deposit and withdraw money
- Transfer funds between accounts
- Check account balances
- Persistent storage using SQLite database
- Transaction history tracking

## Installation

1. Make sure you have Python 3 installed.

2. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

```bash
source venv/bin/activate
```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the application:

```bash
python main.py
```

## Database Structure

The application uses SQLite with two main tables:

### Accounts Table

- account_number (Primary Key)
- holder_name
- balance
- created_at
- status

### Transactions Table

- id (Primary Key)
- account_number (Foreign Key)
- transaction_type
- amount
- timestamp
- related_account (for transfers)
