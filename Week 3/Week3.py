# Created By Brenden Smit

#Problem 3
'''
light_color = input("Enter a light color: ").lower()

if light_color == "green":
    print("Go")
elif light_color == "yellow":
    print("Yield")
elif light_color == "red":
    print("Stop")
else:
    print("Invalid Color")
'''

#Problem 4
'''
age = int(input("Enter your age: "))
athleticism_goal = input("Enter your athleticism goal: ").lower()

if athleticism_goal == "below average":
    if age > 19 and age < 40:
        print('73 - 93')
    elif age > 39 and age < 60:
        print('72 - 94')
    elif age > 59 and age < 80:
        print('71 - 97')
    else:
        print("Invalid Age")
elif athleticism_goal == "above average":
    if age > 19 and age < 40:
        print('47 - 72')
    elif age > 39 and age < 60:
        print('46 - 71')
    elif age > 59 and age < 80:
        print('45 - 70')
    else:
        print("Invalid Age")
else:
    print("Invalid Athleticism Goal")
'''

#Problem 5
'''
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

if num1 < num2 or num3:
    if num2 < num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 < num1 or num3:
    if num1 < num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num2)
else:
    if num1 < num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)
'''

#Problem 6