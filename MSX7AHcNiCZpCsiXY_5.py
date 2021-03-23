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

def how_unlucky(y):
  import datetime as dt
  return sum([dt.date(y,m,13).weekday() == 4 for m in range(1, 12+1)])
