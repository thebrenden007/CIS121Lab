#Problem 1
'''
import random
QuizInts = open("Week 13/QuizInts.txt", "w")
for index in range (100):
    number = random.randint(50,201)
    QuizInts.write(f'{number}\n')
QuizInts.close()
'''
#Problem 2
'''
import random
thisFile = open("Week 13/thisFile.txt", "w")
for index in range (100):
    number = random.randint(50,201)
    thisFile.write(f'{number}\n')
thisFile.close()

thisFile = open("Week 13/thisFile.txt", "r")
thatFile = open("Week 13/thatFile.txt", "w")
for line in thisFile:
    thatFile.write(f'{line}')
thisFile.close()
thatFile.close()
'''
#Problem 3
'''
MyName = open("Week 13/MyName.txt", "w")
MyName.write("Brenden Smit")
MyName.close()
MyName = open("Week 13/MyName.txt", "r")
name = MyName.read().strip()
for letter in name:
    print(letter)
'''
#Problem 5
'''
total_lunches = 0
lunchdata = open("Week 13/LunchData.txt", "r")
for row in lunchdata:
    data = row.split("  ")
    lunches = int(data[1])
    total_lunches += lunches
print(f'The total lunches was {total_lunches}')
'''
#Problem 7
'''
total_visitors = 0
total_days = 0
daily_visits = open('Week 13/LibraryVisits.csv', 'r')
for row in daily_visits:
    data = row.split(",")
    total_visitors += int(data[1])
    total_days += 1
print(f'avg number of visitors at the libray is {total_visitors/total_days}')
'''
#Problem 8
'''
highest_calories_burned = 0
highest_day = ""
calories_burned_data = open("Week 13/CaloriesBurnedData.txt", "r")
for row in calories_burned_data:
    data = row.split("  ")
    calories_burned = int(data[1])
    day = data[0]
    if calories_burned > highest_calories_burned:
        highest_calories_burned = calories_burned
        highest_day = day
print(f'The day with the highest calories burned was {highest_day} with {highest_calories_burned} Calories')
'''
#Problem 11
'''
dict = {}
songplays = open("Week 13/SongPlays.txt", "r")
next(songplays)
for line in songplays:
    data = line.split(" ")
    name = data[0]
    plays = int(data[1])
    if name in dict:
        dict[name] += plays
    else:
        dict[name] = plays

for name, plays in dict.items():
    print(name, plays)
'''