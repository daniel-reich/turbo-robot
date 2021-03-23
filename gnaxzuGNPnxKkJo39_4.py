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
    g = y % 19 + 1
    s = (y - 1600) // 100 - (y - 1600) // 400
    l = ((y - 1400) // 100 * 8) // 25
    p1 = (3 - 11 * g + s - l) % 30
    if p1 == 29 or p1 == 28 and g > 11:
        p = p1 - 1
    else:
        p = p1
    d = (y + y // 4 - y // 100 + y // 400) % 7
    e = p + 1 + (4 - d - p) % 7
    if e < 11:
        return "March " + str(e + 21)
    else:
        return "April " + str(e - 10)

