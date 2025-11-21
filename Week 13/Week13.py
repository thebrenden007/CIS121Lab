#Problem 1
'''
import random
QuizInts = open("Week 13/QuizInts.txt", "w")
for index in range (100):
    number = random.randint(50,201)
    QuizInts.write(f'{number}\n')
QuizInts.close()
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