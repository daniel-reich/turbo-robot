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
    weather = sum([i[1] for i in lst])
    meals = round(sum([i[2]*3.33333333333333 for i in lst]))
    sleep = sum([i[3] for i in lst])
    a = [weather, meals, sleep]
    if weather == meals == sleep:
        return "Nothing"
    elif min(a) == weather:
        return "Weather"
    elif min(a) == meals:
        return "Meals"
    else:
        return "Sleep"
  # lst in format: [Mood, Weather, Meals, Sleep]

