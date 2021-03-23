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
​
def time_to_eat(current_time):
  matches = re.match('(\d+)\:(\d+)', current_time)
  hours = int(matches.group(1)) + (12 if 'p' in current_time else 0)
  minutes = int(matches.group(2))
​
  for meal_time in [7,12,19,31]:
    if hours < meal_time:
      return [meal_time - hours - (minutes != 0), 0 if minutes == 0 else 60 - minutes]

