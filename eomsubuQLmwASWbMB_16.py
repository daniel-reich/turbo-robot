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

import datetime
def weekday_dutch(datein):
    dow = {0:'maandag',
           1:'dinsdag',
           2:'woensdag',
           3:'donderdag',
           4:'vrijdag',
           5:'zaterdag',
           6:'zondag',}
    d, m, y = datein.split()
    dt = datetime.datetime(int(y), int(m), int(d))
    return dow[dt.weekday()]

