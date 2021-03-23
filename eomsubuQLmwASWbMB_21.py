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

import calendar
​
def weekday_dutch(date):
  day, month, year = (int(i) for i in date.split(' '))     
  dayNumber = calendar.weekday(year, month, day) 
  days =["maandag", "dinsdag", "woensdag", "donderdag", 
                         "vrijdag", "zaterdag", "zondag"] 
  return (days[dayNumber])

