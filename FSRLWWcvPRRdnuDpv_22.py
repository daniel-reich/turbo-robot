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

class time:
  def __init__(self, hour, minute):
    self.hour = hour
    self.minute = minute
    
  def time_till(current, target):
    if target.hour > current.hour or target.hour == current.hour and target.minute > current.minute:
      if target.minute >= current.minute:
        return [target.hour - current.hour, target.minute - current.minute]
      else:
        return [target.hour - current.hour - 1, target.minute+60 - current.minute]
    if target.hour < current.hour or target.hour == current.hour and target.minute < current.minute:
      if current.minute == 0:
        return [24 - current.hour + target.hour, current.minute]
      else:
        return [24 - current.hour + target.hour - 1, abs(current.minute - 60)]
    return [0, 0]
    
def time_to_eat(current_time):
  if current_time.index(':') == 2:
    hours = int(current_time[0:2])
    minutes = int(current_time[3:5])
  else:
    hours = int(current_time[0])
    minutes = int(current_time[2:4])
  if current_time[5] == 'p' or current_time[6] == 'p':
    hours += 12
  if current_time[0:2] == '12' and current_time[6] == 'a':
    hours = 0
    
  now = time(hours, minutes)
  breakfast = time(7, 0)
  lunch =  time(12, 0)
  dinner = time(19, 0)
  
  time_to_dinner = time.time_till(now, dinner)
  time_to_lunch =  time.time_till(now, lunch)
  time_to_breakfast = time.time_till(now, breakfast)
  
  if time_to_dinner[0] < time_to_lunch[0] and time_to_dinner[0] < time_to_breakfast[0]:
    return time.time_till(now, dinner)
  if time_to_lunch[0] < time_to_dinner[0] and time_to_lunch[0] < time_to_breakfast[0]:
    return time.time_till(now, lunch)
  return time.time_till(now, breakfast)

