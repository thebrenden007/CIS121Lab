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

word = input("enter a word: ")
pos = 1
for pos in range(1, len(word), 2):
    print(word[pos])

#Problem 3
startnum = 37
endnum = 1050
num = 0

while num > startnum and num < endnum:
    if num % 2 == 0:
        print(num += 1)