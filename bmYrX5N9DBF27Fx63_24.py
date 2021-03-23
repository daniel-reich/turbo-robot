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

import numpy as np
def greatest_impact(lst):
  w,ml,s,format_=[],[],[],['Weather', 'Meals', 'Sleep']
  for el in lst:
    w.append(el[1]/10),ml.append(el[2]/3),s.append(el[3]/10)
  max_var =max([np.std(w),np.std(ml),np.std(s)])
  return 'Nothing' if max_var== 0 else format_[[np.std(w),np.std(ml),np.std(s)].index(max_var)]

