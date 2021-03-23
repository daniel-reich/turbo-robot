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
  a=y%19
  b=y>>2
  c=b//25+1
  d=(c*3)>>2
  e=((a*19)-((c*8+5)//25)+d+15)%30
  e+=(29578-a-e*32)>>10
  e-=((y%7)+b-d+e+2)%7
  d=e>>5
  day=e-d*31
  month=d+3
  if  month==3:
    month="March"+" "+str(day)
    return month
  else:
    month="April"+" "+str(day)
    return month

