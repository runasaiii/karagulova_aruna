class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} accepted. Current balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of {amount} accepted. Current balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")


account = Account("Aruna", 1000)
    
account.deposit(500)  
account.withdraw(200)
account.withdraw(1500) 
account.deposit(-200) 
