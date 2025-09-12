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