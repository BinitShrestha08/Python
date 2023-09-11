class Product:
    def __init__(self, productType, price, quantity):
        self.productType = productType
        self.price = price
        self.quantity = quantity

    
    '''
    class method allows to create object factory
    classmethod kind of constructor/

    cls means class reference
    cls calls initialize

    '''

    @classmethod
    def default_constructor(cls):
        productType = input("Enter product type: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        return cls(productType, price, quantity)

    def isEmpty(self):
        return self.quantity == 0

    def stocked(self, quantity):
        self.quantity += quantity
        return self.price * quantity

    def sold(self, quantity):
        self.quantity -= quantity
        return self.price * quantity

    def has(self, quantity):
        return self.quantity >= quantity

    def cash(self, quantity):
        return self.price*quantity

    def __str__(self):
        formatted_price = "{:.2f}".format(self.price)
        output = self.productType

        output += " Level: " + str(self.quantity) + " at price $" + formatted_price if (
            self.quantity > 0) else " Stock level: " + str(self.quantity)

        return output
