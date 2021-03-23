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
from datetime import date 
import calendar 
​
def weekday_dutch(date):
​
    
    def findDay(date): 
        day, month, year = (int(i) for i in date.split(' '))     
        born = datetime.date(year, month, day) 
        return born.strftime("%A") 
    
    dayd = {'Monday':'maandag','Tuesday':'dinsdag','Wednesday':'woensdag','Thursday':'donderdag','Friday':'vrijdag','Saturday':'zaterdag','Sunday':'zondag' }
    return(dayd[findDay(date)])

