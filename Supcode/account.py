
class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited €{amount}. New balance is €{self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew €{amount}. New balance is €{self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Balance: €{self.balance}")

class CheckingAccount(Account):
    def __init__(self, account_number, holder_name, balance=0):
        super().__init__(account_number, holder_name, balance)

class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, minimum_balance=0):
        super().__init__(account_number, holder_name, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount >= self.minimum_balance:
                self.balance -= amount
                print(f"Withdrew €{amount}. New balance is €{self.balance}.")
            else:
                print(f"Cannot withdraw €{amount}. Minimum balance requirement is €{self.minimum_balance}.")
        else:
            print("Withdrawal amount must be positive.")

    def display_details(self):
        super().display_details()
        print(f"Minimum Balance: €{self.minimum_balance}")

def main():
    # Create a CheckingAccount
    checking_account = CheckingAccount("KM123","Cooper", 1000)
    print("Checking Account Details:")
    checking_account.display_details()
    checking_account.deposit(200)
    checking_account.withdraw(500)
    checking_account.withdraw(1000)
    print()

    # Create a SavingsAccount with a minimum balance requirement
    savings_account = SavingsAccount("LMN889","Caen", 2000, 500)
    print("Savings Account Details:")
    savings_account.display_details()
    savings_account.deposit(300)
    savings_account.withdraw(1000)
    savings_account.withdraw(2000)
    print()

if __name__ == "__main__":
    main()
