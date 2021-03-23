"""


The factors said to have the greatest impact on someone's mood are: weather,
meals, and sleep. Your task is, given a list of sublists of different values
for: Mood, Weather, Meals, and Sleep, determine which other variable has had
the greatest impact on the mood.

### Examples

    greatest_impact([
      [1, 1, 3, 10],
      [1, 1, 3, 10],
      [1, 1, 3, 10]
    ]) ➞ "Weather"
    
    # As it was always low but all others were high.
    
    greatest_impact([
      [10, 10, 3, 10],
      [10, 10, 3, 10],
      [10, 10, 3, 10]
    ]) ➞ "Nothing"
    
    # As all were always high.

### Notes

The mood will always go from 1 to 10, the weather will always go from 1 to 10,
the meals will always go from 1 to 3, and the sleep will always go from 1 to
10. In cases of mood and weather, 1 is negative and 10 is positive. All
sublists values will be in the order `[Mood, Weather, Meals, Sleep]`.

"""

def greatest_impact(lst):
  
  mood_lv = []
  weather = []
  meals_f = []
  sleep_f = []
  final__ = [0, 0, 0, 0]
  diction = {}
​
  for i in range(0, len(lst)):
    x1 = lst[i][0] * 3
    mood_lv.append(x1)
    x2 = lst[i][1] * 3
    weather.append(x2)
    x3 = lst[i][2] * 10
    meals_f.append(x3)
    x4 = lst[i][3] * 3
    sleep_f.append(x4)
​
  for j in range(0, len(mood_lv)):
    final__[0] += mood_lv[j]
    final__[1] += weather[j]
    final__[2] += meals_f[j]
    final__[3] += sleep_f[j]
​
  if final__[1] == final__[2] and final__[2] == final__[3]:
    return "Nothing"
​
  for k in range(0, len(mood_lv)):
    diction["Weather"] = final__[0] / final__[1]
    diction["Meals"] = final__[0] / final__[2]
    diction["Sleep"] = final__[0] / final__[3]
​
​
  diction = sorted(diction.items(), key=lambda item: item[1], reverse = True)
​
  return diction[0][0]

