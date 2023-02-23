# weekday.py
# This program gets the current day of the week and outputs a different message if it a weekday or weekend
# Author: Frank Quinn

#import datetime package
import datetime

# get current date and time
day = datetime.datetime.now()
print('today ',day)

# get the day of the week in number form (format of: 0 = Monday , 6 = sunday)
today = day.weekday()

# check if today is a weekday 
# Saturday is 5 so anything under 5 is a weekday
if today < 5:
    print("Yes, unfortunately today is a weekday")
else:
    print("It's the weekend, yay!")
