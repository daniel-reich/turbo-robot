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

from datetime import datetime as dt
​
def time_to_eat(current_time):
  meal_times = [dt.strptime(i, '%H:%M') for i in ('07:00', '12:00', '19:00')]
  t = dt.strptime(current_time.replace('.', '').upper(), '%I:%M %p')
  nearest = min((m - t).seconds for m in meal_times)
  
  return [nearest//3600, nearest%3600//60]

