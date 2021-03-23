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
    c = 0
    for i in range(1,13):
        if datetime.datetime(y,i,13).strftime('%a')=='Fri':c+=1
    return c

