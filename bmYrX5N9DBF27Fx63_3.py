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

from numpy import corrcoef
def greatest_impact(lst):
    factor_names = ['Weather', 'Meals', 'Sleep']
    mood, weather, meals, sleep = [], [], [], []
    for sub_lst in lst:
        mood.append(sub_lst[0])
        weather.append(sub_lst[1])
        meals.append(sub_lst[2])
        sleep.append(sub_lst[3])
    if len(set(mood)) == 1:
        return 'Nothing'
    correlations = [corrcoef(mood, weather)[0][1], corrcoef(mood, meals)[0][1],
                    corrcoef(mood, sleep)[0][1]]
    max_abs_corr = max(correlations, key=abs)
    return factor_names[correlations.index(max_abs_corr)]

