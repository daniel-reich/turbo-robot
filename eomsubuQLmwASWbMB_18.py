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
    days = {"Monday":"maandag" ,
            "Sunday":"zondag" ,
            "Tuesday":"dinsdag" ,
            "Wednesday":"woensdag",
            "Thursday":"donderdag" ,
            "Friday":"vrijdag",
            "Saturday":"zaterdag"}
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    for i,j in days.items():
        if calendar.day_name[born] == i:
            return (j)

