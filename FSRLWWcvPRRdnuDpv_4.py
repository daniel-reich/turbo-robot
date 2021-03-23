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

def time_to_eat(current_time):
  split_by_space = current_time.split(" ")
  split_by_colon = split_by_space[0].split(":")
  current_hour = int(split_by_colon[0])
  current_minutes = int(split_by_colon[1])
  morning_night = split_by_space[1][0]
  if morning_night == 'p':
    current_hour += 12
  if current_hour < 7:
    hours_til_next = 7 - current_hour
  if 7 <= current_hour < 12:
    hours_til_next = 12 - current_hour
  elif 12 <= current_hour < 19:
    hours_til_next = 19 - current_hour
  elif current_hour >= 19:
    hours_til_next = (24 - current_hour) + 7
  if current_minutes == 0:
    minutes_til_next = current_minutes
  elif current_minutes < 60:
    hours_til_next-=1
    minutes_til_next = 60 - current_minutes
  return [hours_til_next, minutes_til_next]
  
  
  
  
  
  
  
  #return current_hour, current_minutes

