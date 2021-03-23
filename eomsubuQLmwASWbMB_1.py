"""


Write a method that when passed a `date` as "dd mm yyyy" and returns the
date's weekday name in the Dutch culture.

### Examples

    weekday_dutch("21 9 1970") ➞ "maandag"
    
    weekday_dutch(new DateTime("2 9 1945") ➞ "zondag"
    
    weekday_dutch(new DateTime("9 11 2001") ➞ "dinsdag"

### Notes

  * Check the **Resources** tab for help.
  * You can assume the specified date is valid.

"""

from datetime import date
​
dow = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']
def weekday_dutch(dd):
  d, m, y = map(int, dd.split())
  return dow[date(y, m, d).weekday()]

