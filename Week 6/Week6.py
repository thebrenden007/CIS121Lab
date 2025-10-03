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

def war_of_numbers(numbers):
    even_lyst = []
    odd_lyst = []
    for num in numbers:
        if num % 2 == 0:
            even_lyst.append
