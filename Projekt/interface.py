class BankInterface:
    def __init__(self, bank):
        self.bank = bank

    def run(self):
        while True:
            self._display_menu()
            choice = input("\nEnter your choice (1-9): ")
            
            try:
                if choice == '1':
                    self._create_account()
                elif choice == '2':
                    self._close_account()
                elif choice == '3':
                    self._deposit()
                elif choice == '4':
                    self._withdraw()
                elif choice == '5':
                    self._transfer()
                elif choice == '6':
                    self._check_balance()
                elif choice == '7':
                    self._list_accounts()
                elif choice == '8':
                    self._view_transactions()
                elif choice == '9':
                    print("Thank you for using the Bank Management System!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError as e:
                print(f"Error: {e}")
       
    def _display_menu(self):
        print("\n=== Bank Management System ===")
        print("1. Create Account")
        print("2. Close Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Check Balance")
        print("7. List All Accounts")
        print("8. View Transactions")
        print("9. Exit")
     
    def _create_account(self):
        name = input("Enter account holder name: ")
        initial_balance = float(input("Enter initial balance: "))
        account_number = self.bank.create_account(name, initial_balance)
        print(f"Account created successfully! Account number: {account_number}")
    
    def _close_account(self):
        account_number = input("Enter account number to close: ")
        self.bank.close_account(account_number)
        print("Account closed successfully!")
    
    def _deposit(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        self.bank.deposit(account_number, amount)
        print("Deposit successful!")
    
    def _withdraw(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        self.bank.withdraw(account_number, amount)
        print("Withdrawal successful!")
    
    def _transfer(self):
        from_account = input("Enter source account number: ")
        to_account = input("Enter destination account number: ")
        amount = float(input("Enter amount to transfer: "))
        self.bank.transfer(from_account, to_account, amount)
        print("Transfer successful!")
    
    def _check_balance(self):
        account_number = input("Enter account number: ")
        balance = self.bank.get_balance(account_number)
        if balance is not None:
            print(f"Current balance: ${balance:.2f}")
        else:
            print("Account not found!")

    def _list_accounts(self):
        accounts = self.bank.get_all_accounts()
        if not accounts:
            print("No accounts found.")
            return
            
        print("\nAll Bank Accounts:")
        print("-" * 75)
        header = (
            f"{'Account Number':<15} {'Holder Name':<25} "
            f"{'Balance':>10} {'Status':>15}"
        )
        print(header)
        print("-" * 75)
        for account in accounts:
            print(
                f"{account.account_number:<15} {account.holder_name:<25} "
                f"{account.balance:>10.2f} {account.status:>15}"
            )

    def _view_transactions(self):
        account_number = input("Enter account number: ")
        transactions = self.bank.get_transactions(account_number)
        
        if not transactions:
            print("No transactions found for this account.")
            return
            
        print("\nTransaction History:")
        print("-" * 100)
        header = (
            f"{'Type':<15} {'Amount':<12} {'Date':<30} "
            f"{'Related Account':<15}"
        )
        print(header)
        print("-" * 100)
        
        for trans in transactions:
            if trans.transaction_type == 'transfer':
                description = 'Sent to' if trans.amount < 0 else 'Received from'
                related = f"{description} {trans.related_account}"
            else:
                related = ''
            
            print(
                f"{trans.transaction_type:<15} {abs(trans.amount):<12.2f} "
                f"{trans.timestamp:<30} {related:<15}"
            )