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
    
    # Get the first week day of the year
    return len([i for i in [datetime.datetime(y, j, 13).strftime("%A") for j in range(1, 13, 1)] if i == 'Friday'])

