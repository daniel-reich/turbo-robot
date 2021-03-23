"""


The Christian holiday of Easter Sunday is a movable feast. It can occur on any
date from March 22 to April 25. The date depends on the timing between the
Paschal Full Moon and the spring equinox. It wasn't until the late 19th
century that a formula was developed to accurately predict Easter's date for a
given year.

Your task is to use this formula, also known as Butcher's Algorithm, to write
a function that will return the date of Easter for any year after 1600. See
the **Resources** tab for a detailed description of the algorithm.

### Examples

    easter_date(1600) ➞ "April 2"
    
    easter_date(2020) ➞ "April 12"
    
    easter_date(1853) ➞ "March 27"
    
    easter_date(3535) ➞ "April 14"

### Notes

Before 1600 the Julian calendar was used in most countries. The algorithm
we're using is based on the Gregorian calendar, which is still in use today.

"""

def easter_date(y):
    g = y%19 + 1
    s = (y-1600)//100 - (y-1600)//400 
    l = (y-1400)//100 * 8 // 25
    p = (3 - (11*g) + s - l)%30
    
    if p == 29 or (p == 28 and g > 11):
        p -= 1
​
    d = (y + (y//4) - (y//100) + (y//400))%7
    x = ((8-d)%7 - ((3+p)%7)-1)%7 + 1
​
    if p + x < 11:
        easter = 'March {}'.format(round(p + x + 21))
    else:
        easter = 'April {}'.format(round(p + x - 10))
    
    return easter

