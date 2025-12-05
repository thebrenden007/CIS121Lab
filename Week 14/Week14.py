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
#Problem 5
'''
points_dict = {"Alice": 90, "Bob": 75, "Charlie": 60}
try:
    user_name = input("enter a name: ")
    user_points = int(input("enter a score: "))
    points_dict[user_name] += user_points
    print(points_dict[user_name])
except ValueError:
    print("Invalid Number")
except KeyError:
    print("Student not found")
'''
#Problem 7
'''
try:
    num1 = int(input("enter a number: "))
    num2 = int(input("enter another number: "))
    difference = num1 - num2
    ratio = num1 / num2
    print(f'Difference: {difference}, Ratio: {ratio}')
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot divide by zero")
except OverflowError:
    print("Result too large")
'''