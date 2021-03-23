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

from datetime import date, timedelta
def how_unlucky(y):
  d1 = date(y,1,1)
  d2 = date(y,12,31)
  return sum([True for x in range((d2-d1).days+1) if (d1+timedelta(days=x)).weekday() == 4 and (d1+timedelta(days=x)).day==13])

