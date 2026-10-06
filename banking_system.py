class Account:

    def __init__(self, name, account_no, balance=0):
        self.name = name
        self.account_no = account_no
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Account No:", self.account_no)
        print("Balance:", self.balance)

    def show_transactions(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)


# Create account
account = Account("Imran Ali Haider", "FA23-CSE-021", 5000)

account.show_balance()

account.deposit(2000)
account.withdraw(1000)

account.show_balance()
account.show_transactions()
