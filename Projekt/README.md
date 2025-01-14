# Bank Management System

A simple command-line banking application that allows bank employees to manage customer accounts, handle transactions, and maintain records in an SQLite database.

## Features

- Create and close bank accounts
- Deposit and withdraw money
- Transfer funds between accounts
- Check account balances
- Persistent storage using SQLite database
- Transaction history tracking

## Limitations

- Overdraft is not allowed - accounts cannot have negative balances
- Closed accounts cannot be reopened
- Accounts cannot be closed if they have a balance - all money must be withdrawn before closing

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

## Application Structure

The application is divided into several modules:

- `main.py`: Entry point for the application
- `models.py`: Data models representing bank entities; database operations in these models
- `bank.py`: Core banking logic using models defined in `models.py`
- `interface.py`: Handles user interaction and information display

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
