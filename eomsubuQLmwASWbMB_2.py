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
def weekday_dutch(date):
    translate = {'Monday':'maandag','Wednesday':'woensdag','Thursday':'donderdag','Tuesday':'dinsdag','Friday':'vrijdag','Saturday':'zaterdag','Sunday':'zondag'}
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return translate[calendar.day_name[born]]

