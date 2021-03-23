"""


Create a function that takes a list consisting of dice rolls from 1-6. Return
the sum of your rolls with the following conditions:

  1. If a 1 is rolled, that is bad luck. The next roll counts as 0.
  2. If a 6 is rolled, that is good luck. The next roll is multiplied by 2.
  3. The list length will always be 3 or higher.

### Examples

    rolls([1, 2, 3]) ➞ 4
    # The second roll, 2, counts as 0 as a result of rolling 1.
    
    rolls([2, 6, 2, 5]) ➞ 17
    # The 2 following the 6 was multiplied by 2.
    
    rolls([6, 1, 1]) ➞ 8
    # The first roll makes the second roll worth 2, but the
    # second roll was still 1 so the third roll doesn't count.

### Notes

Even if a 6 is rolled after a 1, 6 isn't summed but the 6's "effect" still
takes place.

"""

def rolls(lst):
  array = lst
  for x in range(len(array)):
    if x != 0:
      if array[0 - (x + 1)] == 1:
        array[0 - x] = 0
      elif array[0 - (x + 1)] == 6:
        array[0 - x] *= 2
  return sum(array)
