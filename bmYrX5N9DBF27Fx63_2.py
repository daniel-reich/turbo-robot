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
​
def greatest_impact(lst):
    factors = ["Weather", "Meals", "Sleep"]
    max_val = [10, 3, 10]
    scores = [[],[],[]]
    for part in lst:
        for i in range(1, len(part)):
            scores[i-1].append(part[0] / (part[i] / max_val[i-1]))
    mean = np.array(scores).mean(axis=1)
    if np.max(mean) == np.min(mean):
        return "Nothing"
    return factors[mean.argmax()]

