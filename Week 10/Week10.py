'''
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

bagofcandies = []

candy1 = Candy()
candy1.set_name("KitKat")
candy1.set_shape("Rectangle")
candy1.set_size(10)
candy1.set_price(499.99)
candy1.set_flavor("Chocolate")
print(candy1)

bagofcandies.append(candy1)

for candy in bagofcandies:
    print(candy)
'''
#Problem 1
'''
class Product:
    def __init__(self):
        self.name = 'unknown'
        self.price = 0
        self.quantity = 0
    def get_name(self):
        return self.name
    def set_name(self, value):
        self.name = value
    def get_price(self):
        return self.price
    def set_price(self, value):
        self.price = value
    def get_quantity(self):
        return self.quantity
    def set_quantity(self, value):
        self.quantity = value
    def __str__(self):
        return f'The product is a {self.name}, it cost ${self.price}, and there are {self.quantity} available.'

product1 = Product()
product1.set_name('iPad')
product1.set_price(350)
product1.set_quantity(5)
print(product1)
'''
#Problem 6
'''
class Student:
    def __init__(self, name, major, GPA):
        self.name = name
        self.major = major
        self.GPA = GPA
    def get_name(self):
        return self.name
    def set_name(self, value):
        self.name = value
    def get_major(self):
        return self.major
    def set_major(self, value):
        self.major = value
    def get_GPA(self):
        return self.GPA
    def set_GPA(self, value):
        self.GPA = value
    def introduce(self):
        return f'Hi, I am {self.name}. I am studying {self.major}.'
    def studying(self):
        old_GPA = self.GPA
        self.GPA += 0.2
        if self.GPA > 4.0:
            self.GPA = 4.0
        return f'I am hitting the books! My GPA increased from {old_GPA} to {self.GPA}'
student1 = Student('brenden', 'CIT', 3.5)
print(student1.introduce())
print(student1.get_GPA())
print(student1.studying())
'''
#Problem 9
'''
class Point:
    def __init__(self, xcord, ycord):
        self.xcord = xcord
        self.ycord = ycord
    def get_xcord(self):
        return self.xcord
    def set_xcord(self, value):
        self.xcord = value
    def get_ycord(self):
        return self.ycord
    def set_ycord(self, value):
        self.ycord = value
    def print_info(self):
        return f'(x,y) = ({self.xcord},{self.ycord})'
point1 = Point(5,4)
print(point1.print_info())
'''
#Problem 15
'''
class Recipe:
    def __init__(self):
        self.name = "unknown"
        self.cooktime = 0
    def get_name(self):
        return self.name
    def set_name(self, value):
        self.name = value
    def get_cooktime(self):
        return self.cooktime
    def set_cooktime(self, value):
        self.cooktime = value
    def is_quick_meal(self):
        if self.cooktime < 30:
            return True
        else:
            return False
    def __str__(self):
        return f"The recipe is for {self.name} and takes {self.cooktime} minutes to cook"
    
recipe1 = Recipe()
recipe1.set_name("Alfredo")
recipe1.set_cooktime(35)
print(recipe1)
'''