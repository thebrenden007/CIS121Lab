#Problem 7
'''
def ascending_order(num_1, num_2 = 5, num_3 = 25):
    ascending_lyst = []
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
    if num_1 > num_3:
        num_1, num_3 = num_3, num_1
    if num_2 > num_3:
        num_2, num_3 = num_3, num_2
    return [num_1, num_2, num_3]

print(ascending_order(2,3,1))
'''
#Problem 15

def is_negative(integer):
    if integer < 0:
        return True
    else:
        return False
    
def is_odd(integer):
    if integer % 2 != 0:
        return True
    else:
        return False

def report_negative_odds(integer_lyst):
    negative_odd_lyst = []
    for integer in integer_lyst:
        if is_negative(integer) == True and is_odd(integer) == True:
            negative_odd_lyst.append(integer)
    return negative_odd_lyst

print(report_negative_odds([100,-57,12,1,-36,-15]))