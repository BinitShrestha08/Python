from Product import Product
from CashRegister import CashRegister


class Shop:

    # def __init__(self, product_type, price, quantity):
    def __init__(self):
        # self.product = Product(product_type, price, quantity)
        self.product = Product('Pencil', 3.55, 10)
        self.cash_register = CashRegister()

    def read_quantity(self):
        try:
            quantity = int(input("Quantity: "))
            return quantity
        except ValueError:
            print("Invalid input. Please enter a valid quantity.")
            return self.read_quantity()  # Recursively call read_quantity on invalid input

    def sell(self):
        quantity = self.read_quantity()
        if self.product.has(quantity):
            cash = self.product.sold(quantity)
            self.cash_register.gain(cash)
        else:
            print("Not enough stock!")

    def restock(self):
        quantity = self.read_quantity()
        cash = self.product.cash(quantity)

        if self.cash_register.has(cash):
            cash = self.product.stocked(quantity)
            self.cash_register.pay(cash)
        else:
            print("Not enough funds!")

    def view(self):
        print(self.product)
        print(self.cash_register)

    def readChoice(self):
        choice = input('Choices(s/r/v/x): ')
        return choice

    def help(self):
        print('----------------------')
        print("s: Sale")
        print("r: Restock")
        print("v: View")
        print("x: exit")
        print('----------------------')

    def menu(self):
        char = self.readChoice()
        while char != 'x':

            match(char):
                case 's': self.sell()
                case 'r': self.restock()
                case 'v': self.view()
                case _: self.help()
            # if char == 's':
            #     self.sell()
            # elif char == 'r':
            #     self.restock()
            # elif char == 'v':
            #     self.view()
            # else:
            #     self.help()
            char = self.readChoice()


# if __name__ == "__main__":
#     shop = Shop("Pepsi", 4.5, 10)
#     shop.menu()

def main():
    shop = Shop()
    shop.menu()


if __name__ == "__main__":
    main()
