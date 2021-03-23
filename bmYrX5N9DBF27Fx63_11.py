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

def greatest_impact(factors):
    '''
    Returns the factor (weather, meals, sleep) which has greatest impact on
    mood, given the instructions, or nothing if no single factor predominates.
    '''
    FACTORS = (('Mood',10),('Weather',10),
               ('Meals',3),('Sleep',10))  # Factors and their scales
​
    size = len(factors)
    avgs = [sum(fac)/size/FACTORS[i][1]*100 for i, fac in enumerate(zip(*factors))] 
    if all(avgs[i] == avgs[0] for i in range(1,4)):
        return 'Nothing'
    
    diffs = [abs(avgs[i] - avgs[0]) for i in range(1,4)]
    
    return FACTORS[diffs.index(min(diffs)) + 1][0]

