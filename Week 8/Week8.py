#Problem 1
'''
from random import randint
def toss_coin(guess = 0):
    output = ""
    heads = 0
    tails = 1
    value = randint(0,1)
    if guess == heads and value or guess == tails and value:
        output = "Correct!"
    else:
        output = "Incorrect!"
    return output

print(toss_coin(1))
'''
#Problem 2
'''
from random import randint
def odd_or_even(guess = "even"):
    output = ""
    value = randint(0,1)
    print(value)
    if guess == "even" and value == 0:
        output = "Correct!"
    elif guess == "odd" and value == 1:
        output = "Correct!"
    else:
        output = "Incorrect!"

    return output

print(odd_or_even("even"))
'''
#Problem 3
'''
def count_duplicates(num_1 = 0, num_2 = 0, num_3 = 0):
    count_dict = {}
    x = -1
    num_count = 0
    most_common_num = 0
    output = ""
    numbers = [num_1, num_2, num_3]
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    for nums in count_dict:
        num_count = count_dict[nums]
        if num_count > x:
            most_common_num = nums
            x = num_count
    if num_count == 1:
        output = "Each number is unique"
    else:
        output = (f"There are {num_count} of the same number")

    return output

print(count_duplicates(1,2,3))
'''
#Problem 4
'''
def find_winner(player1 = 'rock', player2 = 'rock'):
    if player1 == player2:
        return "It's a tie!"
    elif player1 == 'rock' and player2 == 'scissor':
        return "Player 1 wins!"
    elif player1 == 'paper' and player2 == 'rock':
        return "Player 1 wins!"
    elif player1 == 'scissors' and player2 == 'paper':
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"
    
print(find_winner("scissors"))
'''
#Problem 6
'''
def hailstone_seq(n = 40):
    lyst = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        elif n % 2 != 0:
            n = ((3 * n) + 1)
        lyst.append(n)
    return lyst

print(hailstone_seq(25))
'''
#Problem 7
'''
def ascending_order(num_1, num_2 = 5, num_3 = 25):
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
    if num_1 > num_3:
        num_1, num_3 = num_3, num_1
    if num_2 > num_3:
        num_2, num_3 = num_3, num_2
    return [num_1, num_2, num_3]

print(ascending_order(2,3,1))
'''
#Problem 8
'''
def descending_order(num_1, num_2 = 15, num_3 = 5):
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1
    if num_1 < num_3:
        num_1, num_3 = num_3, num_1
    if num_2 < num_3:
        num_2, num_3 = num_3, num_2
    return [num_1, num_2, num_3]

print(descending_order(2,45))
'''
#Problem 9
'''
def get_indices(lyst, value = 0):
    pos = []
    for num in range(0, len(lyst)):
        if value == lyst[num]:
            pos.append(num)
    return pos

print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
'''
#Problem 10
'''
def find_factors(number = 36):
    factors = []
    for num in range (1, number + 1):
        if number % num == 0:
            factors.append(num)
    return factors

print(find_factors(12))
'''
#Problem 11
'''
def list_of_multiples(num, length = 5):
    multiples = []
    for number in range(1, length + 1):
        multiples.append(num * number)
    return multiples

print(list_of_multiples(7,5))
'''
#Problem 12
'''
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def report_evens(integer_list):
    even_list = []
    for num in integer_list:
        if is_even(num) == True:
            even_list.append(num)
    return even_list

print(report_evens([4,3,12,16,8,9,25]))
'''
#Problem 13
'''
def is_vowel(letter):
    if letter in ['a','e','i','o','u']:
        return True
    else:
        return False

def report_vowels(word):
    vowel_list = []
    for letter in word:
        if is_vowel(letter) == True:
            vowel_list.append(letter)
    return vowel_list

print(report_vowels("apple"))
'''
#Problem 14
'''
def is_two_digit_number(num):
    if num in range (10, 100):
        return True
    elif num in range (-99, -9):
        return True
    else:
        return False
    
def report_two_digit_numbers(num_list):
    two_digit_list = []
    for num in num_list:
        if is_two_digit_number(num) == True:
            two_digit_list.append(num)
    return two_digit_list

print(report_two_digit_numbers([100,57,12,1]))
'''
#Problem 15
'''
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
'''