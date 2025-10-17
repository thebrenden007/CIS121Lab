#Problem 1
'''
def is_isogram(word):
    letter_dict = {}
    for letter in word:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    for letters in letter_dict:
        if letter_dict[letters] > 1:
            return False
    return True

word1 = "algorism"
word2 = "password"
print(is_isogram(word1))
print(is_isogram(word2))
'''
#Problem 2
'''
def find_unique(num_lyst):
    num_dict = {}
    unique_num_lyst = []
    for num in num_lyst:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    for number in num_dict:
        num_count = num_dict[number]
        if num_count < 2:
            unique_num_lyst.append(number)
    return unique_num_lyst

num_lyst = [1,2,2,3,3,4,4]
print(find_unique(num_lyst))
'''
#Problem 3
'''
def return_unique(num_lyst):
    num_dict = {}
    unique_num_lyst = []
    for num in num_lyst:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    for number in num_dict:
        num_count = num_dict[number]
        if num_count < 2:
            unique_num_lyst.append(number)
    return unique_num_lyst

num_lyst = [1,9,8,8,7,6,1,6]
print(return_unique(num_lyst))
'''
#Problem 4
'''
def get_names(names):
    name_lyst = []
    for key in names:
        name = names[key]
        name_lyst.append(name)
    return name_lyst

id_dict = {"ID1": "John", "ID2": "Emma", "ID3": "Liam"}
print(get_names(id_dict))
'''
#Problem 5
'''
def find_oldest(people):
    oldest_age = -1
    oldest_name = ""
    for name in people:
        age = people[name]
        if age > oldest_age:
            oldest_age = age
            oldest_name = name
    return oldest_name

people_dict = {"Emma": 71, "Jack": 45, "Olivia": 82, "Liam": 39}
print(find_oldest(people_dict))
'''
#Problem 6
'''
def letter_count(word):
    letter_dictionary = {}
    for letter in word:
        if letter in letter_dictionary:
            letter_dictionary[letter] += 1
        else:
            letter_dictionary[letter] = 1

    return letter_dictionary

print(letter_count("hello"))
'''
#Problem 7
'''
def min_grade(exams):
    low_grade_num = 100
    low_grade_class = ""
    for school_class in exams:
        grade = exams[school_class]
        if grade < low_grade_num:
            low_grade_num = grade
            low_grade_class = school_class
    return low_grade_class

exams = {"Physics": 82, "Math": 65, "History": 75, "Biology": 95, "English": 87}
print(min_grade(exams))
'''
#Problem 8
'''
def find_youngest(people):
    yougest_age = 100
    youngest_name = ""
    for name in people:
        age = people[name]
        if age < yougest_age:
            youngest_age = age
            youngest_name = name
    return youngest_name

people_dict = {"Emma": 71, "Jack": 45, "Olivia": 82, "Liam": 39}
print(find_youngest(people_dict))
'''
#Problem 9
'''
receipt = {"Side Salad": 6, "Chicken Parm": 12, "Cookie": 3}
total_price = 0
for value in receipt:
    price = receipt[value]
    total_price += price
print(total_price)
'''
#Problem 10
'''
menu = {"burger": 10, "fries": 4, "soda": 3}
for item in menu:
    price = menu[item]
    print(f"{item} cost {price}")
'''
#Problem 11
'''
def count_repetitions(elements):
    count_dict = {}
    for item in elements:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

lyst1 = ["cat", "dog", "cat", "cow", "cow", "cow"]
lyst2 = ["infinity", "null", "infinity", "null", "null"]
print(count_repetitions(lyst1))
print(count_repetitions(lyst2))
'''
#Problem 12
'''
def item_purchase(store, wallet):
    afford_lyst = []
    for item in store:
        price = store[item]
        if price < wallet + 1:
            afford_lyst.append(item)
    return afford_lyst

store = {"Water": 1, "Bread": 3, "TV": 1000}
wallet = int(input("enter a budget: "))
print(item_purchase(store, wallet))
'''
#Problem 13
'''
def total_sales(sales):
    total_price = 0
    for value in sales:
        price = sales[value]
        total_price += price
    return total_price
sales = {"Laptop": 5, "Phone": 10, "Tablet": 3}
print(total_sales(sales))
'''
#Problem 14
'''
def high_earners(employee_salaries, given_salary):
    high_earn_people = []
    for name in employee_salaries:
        earn = employee_salaries[name]
        if earn > given_salary:
            high_earn_people.append(name)
    return high_earn_people

employee_salaries = {"Alice": 50000, "Bob": 75000, "Charlie": 100000}
given_salary = int(input("enter a salary: "))
print(high_earners(employee_salaries, given_salary))
'''
#Problem 16
'''
def total_calories(fruits):
    calories = {"apple": 95, "banana": 105, "orange": 62, "grape": 3, "pear": 102}
    total_calories = 0
    for fruit in fruits:
        total_calories += calories[fruit]

    return total_calories

print(total_calories(["apple", "banana", "orange"]))
'''
#Problem 17
'''
def total_cost(ingredients):
    cost = 0
    prices = {"flour": 2.50, "sugar": 1.80, "eggs": 3.00, "milk": 2.00, "butter": 2.75, "vanilla": 4.50, "chocolate": 5.00}
    for ingredient in ingredients:
        cost += prices[ingredient]

    return cost

print(total_cost(["flour", "sugar", "eggs", "butter"]))
'''
#Problem 18
'''
def majority_element(nums):
    num_dict = {}
    most_occurence = -1
    majority_num = 0
    for num in nums:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    for number in num_dict:
        occurence = num_dict[number]
        if occurence > most_occurence:
            most_occurence = occurence
            majority_num = number
    return majority_num

print(majority_element([3,2,3]))
'''