"""


A long stretch of beach is represented by a string of two characters `0` \-
free, `1` \- occupied. Due to recent restrictions, a new person cannot take
place next to another. There has to be one free place between two people
lounging on the beach. Create a function to compute how many new people at
most can settle in on the given beach.

### Examples

    sun_loungers("10001") ➞ 1
    # Can take place in the middle.
    
    sun_loungers("00101") ➞ 1
    # Can take place on the left.
    
    sun_loungers("0") ➞ 1
    # Can take one place.
    
    sun_loungers("000") ➞ 2
    # Can take places on the left and on the right.

### Notes

N/A

"""

import re
def sun_loungers(beach):
  if beach == "0":
    return 1
  n = 0
  if beach[:2] == "00":
    beach = "1" + beach[1:]
    n += 1
  if beach[-2:] == "00":
    beach = beach[:-1] + "1"
    n += 1
  res = sum([ (len(x)-1)//2  for x in re.findall(r"(0+)",beach)])
  return res +n

