"""


Create a function which returns how many **Friday 13ths** there are in a given
year.

### Examples

    how_unlucky(2020) ➞ 2
    
    how_unlucky(2026) ➞ 3
    
    how_unlucky(2016) ➞ 1

### Notes

Check **Resources** for some helpful tutorials on the Python `datetime`
module.

"""

import calendar
def how_unlucky(y):
  sum = 0
  for month in range(1,13):
    if calendar.weekday(y,month,13) == 4:
      sum += 1
  return sum

