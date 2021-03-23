"""


Given the `month` and `year` as numbers, return whether that month contains a
**Friday 13th**.

### Examples

    has_friday_13(3, 2020) ➞ True
    
    has_friday_13(10, 2017) ➞ True
    
    has_friday_13(1, 1985) ➞ False

### Notes

  * January will be given as `1`, February as `2`, etc ...
  * Check **Resources** for some helpful tutorials on Python's `datetime` module.

"""

import datetime
​
def has_friday_13(month, year):
    d = datetime.datetime(year, month, 13)
    return int(d.strftime('%w')) == 5
​
    print(has_friday_13(10, 2020))
