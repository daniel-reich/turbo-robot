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

from math import floor
def easter_date(year):
  a, b, c = year % 19, year % 4, year % 7
  k = floor(year / 100)
  p, q = floor((13 + 8 * k) / 25), floor(k / 4)
  M, N = (15 - p + k - q) % 30, (4 + k - q) % 7
  d = (19 * a + M) % 30
  e = (2 * b + 4 * c + 6 * d + N) % 7
  mar = 22 + d + e
  apr = d + e - 9
  return 'March ' + str(mar) if 22 <= mar <= 31 else "April " + str(apr)

