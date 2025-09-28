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
#Problem 2

def is_fever(temperature):
    
    if temperature[-1] == "F":
        if temperature[:-1] > 98.6:
            return True
        else:
            return False
    if temperature[-1] == "C":
        if temperature[0:-1] > 37:
            return True
        else:
            return False

    return True