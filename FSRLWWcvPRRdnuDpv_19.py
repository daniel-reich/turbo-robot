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
  suffix = "".join([i for i in current_time if i.isalpha()])
  hour = int("".join([i for i in current_time[:current_time.find(":")]]))
  minute = int("".join([i for i in current_time[current_time.find(":"):] if i.isdigit()]))/60
  times = [7, 12, 19]
  if suffix == "pm" and hour != 12:
    hour += 12
  print(hour)
  print(minute*60)
  while True:
    for i in times:
      if i - (hour + minute) > 0:
        print(i)
        return [i - hour if minute == 0 else i - hour - 1, int(60*minute) if minute == 0 else int(60-60*minute)]
    times = [31]
print(time_to_eat("5:50 a.m."))

