#Problem 1
'''
larger = int(input("enter a number: "))
smaller = int(input("enter a smaller number: "))

counter  = 0
while (larger / 2 > smaller):
    larger/=2
    counter += 1
print(counter)
'''
#Problem 2
'''
word = input("enter a word: ")
pos = 1
for pos in range(1, len(word), 2):
    print(word[pos])
'''
#Problem 3
'''
num = 0

for num in range (37,1050 +1):
    if num % 2 == 0:
        print(num)
'''
#Problem 4
'''
word = ''
done = False
while not done:
    letter = input("enter a letter (or type done): ")
    if letter != 'done':
        word += letter
        print(letter)
    else:
        done = True
print(word)
'''
#Problem 5'
'''
num = 0
total = 0
for num in range (50,517 +1):
    if num % 2 != 0:
        total += num
print(total)
'''
#Problem 6
'''
total = 0
done = False
while not done:
    integer = int(input("enter an integer: "))
    if integer > 0:
        total += int(integer)
    else:
        done = True
print(total)
'''
#Problem 7
