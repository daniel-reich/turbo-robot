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
  ones = []
  for i in range(len(beach)):
    if beach[i] == '1':
      ones.append(i)
  
  if not ones:
    return (len(beach)+1)//2
  
  ans = sum((b-a-2)//2 for a,b in zip(ones, ones[1:]))
  ans += ones[0]//2
  ans += (len(beach) - ones[-1]-1)//2
  
  return ans

