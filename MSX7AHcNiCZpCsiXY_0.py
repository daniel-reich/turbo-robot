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

from datetime import date
​
def how_unlucky(y):
  return sum(date(y, m, 13).strftime('%A') == 'Friday' for m in range(1, 13))

