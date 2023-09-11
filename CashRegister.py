class CashRegister:
    '''Constructor method to initialize fields'''

    def __init__(self):
        self.cash = 0.0

    def gain(self, amount: float):
        self.cash += amount

    def pay(self, amount: float):
        self.cash -= amount

    def isEmpty(self):
        return self.cash == 0

    def has(self, cash):
        '''if objects cash is greater than equals to paramter cash
            differentiate by self
        '''
        return self.cash >= cash

    def __str__(self):
        formated = "{:.2f}".format(self.cash)
        return "Cash Level: $" + formated if not self.isEmpty() else "Cash register is empty"
