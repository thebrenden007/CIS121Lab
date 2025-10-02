#Functions
#Problem 1
'''
def pyramid_volume(user_base, user_height):
    volume_output = ""

    volume_output = (((user_base ** 2) * user_height) / 3)
    return volume_output

input_base = int(input("enter the base: "))
input_height = int(input("enter the height: "))

print(f"The volume is: {pyramid_volume(input_base, input_height)}")
'''
#Problem 2
'''
def cone_volume(user_radius, user_height):
    volume_output = ""
    import math
    volume_output = ((math.pi) * (((user_radius ** 2) * user_height) / 3))
    return volume_output

input_radius = int(input("enter the radius: "))
input_height = int(input("enter the height: "))
print(f"The volume is: {cone_volume(input_radius, input_height)}")
'''
#Problem 3
'''
def total_score(two_pointers, three_pointers):
    score_output = ""

    score_output = (two_pointers * 2) + (three_pointers * 3)
    return score_output

two_input = int(input("number of two pointers: "))
three_input = int(input("number of three pointers: "))
print(f"The total score is {total_score(two_input, three_input)}")
'''
#Problem 8
'''
def pool_time(user_grade, user_time):
    time_output = ""

    if user_grade == "K":
        user_grade == 0
    
    if 0 <= int(user_grade) <= 3:
        if user_time == "Morning":
            time_output = "9am"
        else:
            time_output = "1pm"
    elif 4 <= int(user_grade) <= 8:
        if user_time == "Morning":
            time_output = "10am"
        else:
            time_output = "2pm"
    else:
        if user_time == "Morning":
            time_output = "11am"
        else:
            time_output = "3pm"

    return time_output

input_grade = input("Enter Grade: ")
input_time = input("Enter Time: ")

print(f"The pool Time is: {pool_time(input_grade, input_time)}")
'''
#Problem 11
'''
def convert_knuts(knuts):
    output = ""
    
    galleons= knuts // (29 * 17)
    knuts_remaining = knuts % (29 * 17)
    sickles =  knuts_remaining // 29
    knuts_final = knuts_remaining % 29

    if galleons > 0:
        output = output + f"Galleons: {galleons} "
    if sickles > 0:
        output = output +  f"sickles: {sickles} "
    if knuts_final > 0:
        output = output + f"knuts: {knuts_final}"

    return output

user_input = int(input("enter amount of knuts: "))
print(f"For {user_input} knuts I can buy: {convert_knuts(user_input)}")
'''

#Strings
#Problem 1
'''
def reverse_string(word):
    reversed_word = word[::-1]
    return reversed_word
user_word = input("enter a word: ")
print(f"{reverse_string(user_word)}")
'''
#Problem 2
'''
def is_fever(input):
    unit = input[-1]
    temperature = int(input[:-1])
    output = False
    if unit == "F":
        if temperature > 98.6:
            output = True
    elif unit == "C":
        if temperature > 37:
            output = True

    return output

user_input = input("Enter a temperature 00F or 00C: ")
print(f"{is_fever(user_input)}")
'''
#Problem 3
'''
def is_boiling(input):
    unit = input[-1]
    temperature = int(input[:-1])
    output = False
    if unit == "F":
        if temperature >= 212:
            output = True
    elif unit == "C":
        if temperature >= 100:
            output = True
    return output

user_input = input("Enter a temperature 000F or 000C: ")
print(f"{is_boiling(user_input)}")
'''