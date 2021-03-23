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
import calendar
days = {0:'zon',1:'maan',2:'dins',3:'woens',4:'donder',5:'vrij',6:'zater'}
def weekday_dutch(date):
  day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
  return days[(day+1)%7] + 'dag'

