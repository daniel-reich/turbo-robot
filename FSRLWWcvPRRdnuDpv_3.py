"""


Jake is a very habitual person. He eats breakfast at 7:00 a.m. each morning,
lunch at 12:00 p.m. and dinner at 7:00 p.m. in the evening.

Create a function that takes in the current time as a string and determines
the duration of time before Jake's next meal. Represent this as a list with
the first and second elements representing hours and minutes, respectively.

### Examples

    time_to_eat("2:00 p.m.") ➞ [5, 0]
    // 5 hours until the next meal, dinner
    
    time_to_eat("5:50 a.m.") ➞ [1, 10]
    // 1 hour and 10 minutes until the next meal, breakfast

### Notes

N/A

"""

import re
import datetime
​
def time_to_eat(current_time):
  current_time = re.sub('\.', '', current_time).upper()
  dt = datetime.datetime.strptime(current_time, '%I:%M %p')
  hour = dt.hour + dt.minute/60
  if (hour <= 7):
    result = 7 - hour
  elif (hour <= 12):
    result =  12 - hour
  elif (hour <= 19):
    result =  19 - hour
  else:
    result =  24 - hour + 7
  return [int(result), round(60*(result-int(result)))]

