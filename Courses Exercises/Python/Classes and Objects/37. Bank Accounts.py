class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, money):
        self.balance = self.balance+ money
        return self.balance
    
    def withdraw(self, money):
        self.balance = self.balance - money
        return self.balance
    
    def display_balance(self):
        print("Your bank account has: $" + str(self.balance))

Romel_Account = BankAccount("Romel", "Ontiveros", 571002007, "Debit", 2007, 1000.0) 

Romel_Account.deposit(96)
Romel_Account.withdraw(25)
Romel_Account.display_balance()
