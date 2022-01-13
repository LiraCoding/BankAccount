class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.04, balance=0): 
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit Complete") 
        return self

    def withdraw(self, amount):
        if (self.balance - amount < 0):
            print("insufficient funds:Charging fee=$10.00")
        else:
            self.balance -= amount
        print("The remaining balance is:", self.balance)
        return self

    def display_account_info(self):
        print("The remaining balance is:", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
          self.balance += self.balance * self.int_rate
        print(self.balance)
        print(self.int_rate)
        return(self)  

rays_bank_account = BankAccount(2600, 0.03)
scotts_bank_account = BankAccount(13000, 0.05)

rays_bank_account.deposit(300).deposit(2000).deposit(5000).withdraw(200).yield_interest().display_account_info()
print("Ray's balance is:", rays_bank_account.balance)

scotts_bank_account.deposit(500).deposit(500).withdraw(30).withdraw(100).withdraw(150).withdraw(90).yield_interest().display_account_info()
print("Scott's balance is:", scotts_bank_account.balance)


