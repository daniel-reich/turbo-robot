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
  split = current_time.index(":")
  hour = int(current_time[:split])
  if current_time[-4::] == "p.m.":
    hour += 12
  mins = int(current_time[split+1:split+3])
  if hour < 7:
    hoursuntil = 6 - hour
    minsuntil = 60 - mins
  elif hour < 12:
    hoursuntil = 11 - hour
    minsuntil = 60 - mins
  elif hour < 19:
    hoursuntil = 18 - hour
    minsuntil = 60 - mins
  else:
    hoursuntil = 30 - hour
    minsuntil = 60 - mins
  if minsuntil == 60:
    minsuntil = 0
    hoursuntil += 1
  return [hoursuntil, minsuntil]

