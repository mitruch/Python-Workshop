import  random

class BankAccount:
    def __init__(self):
        self.amount = 0

    def get_balance(self):
        return self.amount
    
    def deposit(self, amount, with_promo=False):
        p = random.random()
        if p < 0.1 and with_promo is True:
            

        self.amount += amount