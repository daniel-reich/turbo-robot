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

def weekday_dutch(date):
    import datetime
    import calendar
    day, month, year = (int(i) for i in date.split(' '))
    dayNumber = calendar.weekday(year, month, day)
    englishtodutch = {0: "maandag", 1: 'dinsdag', 2: 'woensdag', 3: 'donderdag', 4: 'vrijdag', 5: 'zaterdag', 6: 'zondag'}
    return(englishtodutch[dayNumber])

