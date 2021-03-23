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

import math
​
timeAddons = {'a.m.':0,'p.m.':12}
times = [7,12,19]
​
def findNextInList(iterable,item):
  index = 0
  for i in range(len(iterable)):
    if item > iterable[i]:
      index+=1
    if index == 3:
      index = 0
  return index
    
def time_to_eat(current_time):  
  formattedTime = current_time.split(' ')
  
  currentHours = int(formattedTime[0].split(':')[0])+timeAddons[formattedTime[1]]
  currentMinutes = int(formattedTime[0].split(':')[1])
  print(currentHours,currentMinutes)
  
  indexO = findNextInList(times,currentHours)
  
  while True:
    targetTime = times[indexO]
    print(targetTime)
​
    minuteDistance = 60 - currentMinutes
    if minuteDistance == 60:
          minuteDistance = 0
    print(minuteDistance)
    hourDistance = targetTime-currentHours-math.ceil(minuteDistance/60)
    print(hourDistance)
    if hourDistance == 0 and minuteDistance == 0:
      indexO +=1
      print("added one")
    else:
      break
  
  if hourDistance < 0:
    hourDistance += 24
  
  print([hourDistance,minuteDistance])
  return [hourDistance,minuteDistance]

