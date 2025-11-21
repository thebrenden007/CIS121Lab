#Problem 1
'''
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        else:
            return False
    def __add__(self, other):
        combined_a = self.a + other.a
        combined_b = self.b + other.b
        new_vector = Vector(combined_a, combined_b)
        return new_vector
    def __str__(self):
        #return f'This vector has an x of {self.a} and a y of {self.b}'
        return f'v = {self.a}x + {self.b}y'

v1 = Vector(2,3)
v2 = Vector(2,3)
v3 = Vector(4,5)
new_v = v1 + v3
print(new_v)
'''
#Problem 4

class LinearEquation:
    def __init__(self, m, b):
        self.m = m
        self.b = b
    def __add__
#Problem 8
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __mul__(self, num):
        multiplied_width = self.width * num
        multiplied_height = self.height * num
        return Rectangle(multiplied_width, multiplied_height)
    def __str__(self):
        return f"Rectangle ({self.width} x {self.height})"
r1 = Rectangle(4,5)
r2 = Rectangle(3,2)
print(r1 * 3)
'''
#Problem 9
'''
class Playlist:
    def __init__(self, name = "New Playlist", songs = []):
        self.name = name
        self.songs = songs
    def add_song(self, song):
        self.songs.append(song)
    def __add__(self, other):
        combined_name = f'{self.name} & {other.name}'
        combined_songs = self.songs + other.songs
        return Playlist(combined_name, combined_songs)
    def __str__(self):
        return f"{self.name} playlist has these songs: {self.songs}"

p1 = Playlist("Christmas", ["Jingle Bells", "Mr. Grinch"])
p2 = Playlist("Country", ["Last Night", "What I Want"])
p1.add_song("Mistle Toe")
new_p = p1 + p2
print(new_p)
'''
#Problem 10
'''
class ShoppingCart:
    def __init__(self, items = {}):
        self.items = items
    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1
    def __add__(self, other):
        combined = ShoppingCart()
        for item, qty in self.items.items():
            combined.items[item] = qty
        for item, qty in other.items.items():
            if item in combined.items:
                combined.items[item] += qty
            else:
                combined.items[item] = qty
        return combined
    def __str__(self):
        return f'{self.items}'
    
cart1 = ShoppingCart({"tea" : 1, "energy drink" : 2})
cart1.add_item("sandwich")
cart2 = ShoppingCart({"energy drink" : 3, "hat" : 1})
combined = cart1 + cart2
print(combined)
'''