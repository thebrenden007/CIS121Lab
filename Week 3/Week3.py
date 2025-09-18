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

#Problem 
'''
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

if num1 < num2 and num1 < num3:
    if num2 < num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 < num1 and num2 < num3:
    if num1 < num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    if num1 < num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)
'''

#Problem 6
'''
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

if num1 > num2 and num > num3:
    if num2 > num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    if num1 > num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)
'''

#Problem 7
'''
knuts = int(input("enter amount of knuts: "))
galleons = knuts // (29 * 17)
knuts_remaining = knuts % (29 * 17)
sickles =  knuts_remaining // 29
knuts_final = knuts_remaining % 29

output = ""
if galleons > 0:
    output.append(f"{galleons} galleon{'s' if galleons > 1 else ''}")
if sickles > 0:
    output.append(f"{sickles} sickle{'s' if sickles > 1 else ''}")
if knuts_final > 0:
    output.append(f"{knuts_final} knuts")
print(output)
'''

#Problem 8
'''
num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))
num3 = int(input("enter another number: "))

if num1 > num2 and num1 > num3:
    print(f'The largest number is {num1}')
elif num2 > num1 and num2 > num3:
    print(f'The largest number is {num2}')
else:
    print(f'The largest number is {num3}')
'''