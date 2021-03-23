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

def greatest_impact(x):
  for i in x: i[2] = i[2]*10/3
  y = [sum(abs(x[i][j] - x[i][0]) for i in range(len(x))) for j in range(1, 4)]
  if len(set(y)) < 3: return 'Nothing'  
  if y.index(min(y)) == 0: return 'Weather'
  if y.index(min(y)) == 1: return 'Meals'
  if y.index(min(y)) == 2: return 'Sleep'

