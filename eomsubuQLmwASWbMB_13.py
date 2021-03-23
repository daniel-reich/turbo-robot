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
    list1=date.split(' ')
    day1=datetime.date(int(list1[2]),int(list1[1]),int(list1[0])).isoweekday()
    if day1 == 1:
        return 'maandag'
    elif day1 == 2:
        return 'dinsdag'
    elif day1 == 3:
        return 'woensdag'
    elif day1 == 4:
        return 'donderdag'
    elif day1 == 5:
        return 'vrijdag'
    elif day1 == 6:
        return 'zaterdag'
    elif day1 == 7:
        return 'zondag'

