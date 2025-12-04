#Problem 1
'''
try:
    user_input = int(input("enter a number: "))
    output = 10 / user_input
    print(output)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
'''
#Problem 2
'''
fruit = ["apple", "banana", "cherry", "date"]
try:
    user_input = int(input("enter an index: "))
    print(fruit[user_input])
except ValueError:
    print("Invalid Index Format")
except IndexError:
    print("Index out of range")
'''