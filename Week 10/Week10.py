class Candy:
    def __init__(self):
        self.name = "unknown"
        self.flavor = "unknown"
        self.shape = "unknown"
        self.size = "unknown"
        self.price = 0

    def get_name(self):
        return self.name
    def set_name(self, value):
        self.name = value
    def get_price(self):
        return self.price
    def get_price_cad(self):
        return self.price * 1.4
    def set_price(self, value):
        if 0 <= value < 1000:
            self.price = value
    def get_shape(self):
        return self.shape
    def set_shape(self, value):
        self.shape = value
    def get_size(self):
        return self.size
    def set_size(self, value):
        self.size = value
    def get_flavor(self):
        return self.flavor
    def set_flavor(self, value):
        self.flavor = value
    def reaction(self):
        if 0 < self.size < 5:
            return "try again next time, its too small!!"
        elif 5 < self.size < 10:
            return "Ehhh i guess its okay"
        else:
            return "WOW!!!"
    def __str__(self):
        return f"{self.name} its {self.flavor} cost {self.price} and is of size and shape {self.size}, {self.shape} {self.reaction()}"
    
candy1 = Candy()
candy1.set_name("KitKat")
candy1.set_shape("Rectangle")
candy1.set_size(10)
candy1.set_price(499.99)
candy1.set_flavor("Chocolate")
print(candy1)