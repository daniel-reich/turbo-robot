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

def sun_loungers(beach):
  beach = list(beach)
  if len(beach) < 2:
    return 1 if beach == ['0'] else 0
  if beach[0] == beach[1] == '0':
    beach[0] = 2
  for i in range(1,len(beach)-1):
    if beach[i] == '0' and beach[i-1] == '0' and beach[i+1] == '0':
      beach[i] = 2
  if beach[-2] == beach[-1] == '0':
    beach[-1] = 2
  return beach.count(2)

