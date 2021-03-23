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

import datetime
import calendar
def how_unlucky(y):
  d = 32
  m = 13
  f = []
  for i in range(1,m):
    for j in range(1,d):
      try: 
        date = datetime.date(y,i,j)
        if calendar.day_name[date.weekday()] == "Friday" and j == 13:
          f.append(date)
      except:
        pass
  return len(f)

