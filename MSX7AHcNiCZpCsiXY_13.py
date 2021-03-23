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
def how_unlucky(y):
  count = 0
  for i in range(1,13):
    day = datetime.datetime.strftime(datetime.datetime.strptime(("13"+" "+str(i)+" "+str(y)),"%d %m %Y"),"%A")
    if day == "Friday": 
      count +=1
  return count

