#Problem 1
'''
def skip_letter(word):
    lyst = []
    pos = 0
    for pos in range(0, len(word), 2):
        lyst.append(word[pos])
    return lyst

user_word = input("enter a word: ")
print(f"{skip_letter(user_word)}")
'''
#Problem 2
'''
def skip_letter(word):
    lyst = []
    pos = 1
    for pos in range(1, len(word), 2):
        lyst.append(word[pos])
    return lyst

user_word = input("enter a word: ")
print(f"{skip_letter(user_word)}")
'''
#Problem 3
'''
def output_even(smaller_num, larger_num):
    num_lyst = []
    for num in range (smaller_num, larger_num + 1):
        if num % 2 == 0:
            num_lyst.append(num)
    return num_lyst

small_num = int(input("enter a small number: "))
large_num = int(input("enter a larger number: "))
print(f"{output_even(small_num, large_num)}")
'''
#Problem 4
'''
def output_odd(smaller_num, larger_num):
    num_lyst = []
    for num in range (smaller_num, larger_num + 1):
        if num % 2 != 0:
            num_lyst.append(num)
    return num_lyst

small_num = int(input("enter a small number: "))
large_num = int(input("enter a larger number: "))
print(f"{output_odd(small_num, large_num)}")
'''
#Problem 5
'''
def hailstone_seq(n):
    lyst = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            lyst.append(n)
        elif n % 2 != 0:
            n = ((3 * n) + 1)
            lyst.append(n)
    return lyst

num = int(input("enter an integer: "))
print(f"{hailstone_seq(num)}")
'''
#Problem 6
'''
def find_factors(num):
    factors = []
    for number in range (1, num +1):
        if num % number == 0:
            factors.append(number)
    return factors

user_num = int(input("enter a number: "))
print(f"{find_factors(user_num)}")
'''
#Problem 9
'''
def count(cards):
    card_count = 0
    for card in cards:
        if card in range (2, 7):
            card_count += 1
        elif card in [10, "j", "q", "k", "a"]:
            card_count -= 1
    return card_count

user_cards1 = [5, 9, 10, 3, "j", "a", 4, 8, 5]
user_cards2 = ["a", "a", "k", "q", "q", "j"]
user_cards3 = ["a", 5, 5, 2, 6, 2, 3, 8, 9, 7]
print(f"{count(user_cards1)}")
print(f"{count(user_cards2)}")
print(f"{count(user_cards3)}")
'''
#Problem 10
'''
def war_of_numbers(numbers):
    output = ''
    even_total = 0
    odd_total = 0
    for num in numbers:
        if num % 2 == 0:
            even_total += num
        else:
            odd_total += num
    if even_total > odd_total:
        output = "Evens"
    else:
        output = "Odds"
    return output

user_numbers1 = [2,8,7,5]
user_numbers2 = [12,90,75,1,1]
user_numbers3 = [2,10,22,243]
print(f"{war_of_numbers(user_numbers1)}")
print(f"{war_of_numbers(user_numbers2)}")
print(f"{war_of_numbers(user_numbers3)}")
'''
#Problem 11
'''
def add_lists(lyst1, lyst2):
    combined_lyst = []
    for num in range(len(lyst1)):
        combined_lyst.append(lyst1[num] + lyst2[num])
    return combined_lyst

lyst1 = [1,3,3,1]
lyst2 = [4,3,6,1]
print(f"{add_lists(lyst1, lyst2)}")
'''
#Problem 12
'''
def largest_even(numbers):
    largest = -1
    for num in numbers:
        if num % 2 == 0 and num > largest:
            largest = num
    return largest

numbers = [3,7,2,1,7,9,10,13]
print(f"{largest_even(numbers)}")
'''
#Problem 13
'''
def largest_odd(numbers):
    largest = -1
    for num in numbers:
        if num % 2 != 0 and num > largest:
            largest = num
    return largest

numbers = [3,7,2,1,7,9,10,13]
print(f"{largest_odd(numbers)}")
'''
#Problem 14
'''
def progress_days(miles):
    progress = 0
    for pos in range(1, len(miles)):
        if miles[pos] > miles[pos-1]:
            progress += 1
    return progress

miles = [3,4,1,2]
print(f"{progress_days(miles)}")
'''
#Problem 15
'''
def lag_days(miles):
    lag = 0
    for pos in range(1, len(miles)):
        if miles[pos] < miles[pos-1]:
            lag += 1
    return lag

miles = [5,3,2,1]
print(f"{lag_days(miles)}")
'''
#Problem 16

def like_or_dislike(events):
    state = "nothing"
    for event in events:
        if event == "like" and state != "like":
            state = "like"
        elif event == "dislike" and state != "dislike":
            state = "dislike"
        else:
            state = "nothing"
    return state

events1 = ["dislike"]
events2 = ["like", "like"]
events3 = ["dislike", "like"]
events4 = ["like", "dislike", "dislike"]
print(f"{like_or_dislike(events1)}")
print(f"{like_or_dislike(events2)}")
print(f"{like_or_dislike(events3)}")
print(f"{like_or_dislike(events4)}")