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

def easter_date(year):
    dic = {1: "January",
         2: "February",
         3: "March",
         4: "April",
         5: "May",
         6: "June",
         7: "July",
         8: "August",
         9: "September",
         10: "October",
         11: "November",
         12: "December"
         }
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1
    return '{} {}'.format(dic[month], day)

