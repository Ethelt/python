from bank import Bank
from interface import BankInterface

def main():
    bank = Bank()
    interface = BankInterface(bank)
    interface.run()

if __name__ == "__main__":
    main()
