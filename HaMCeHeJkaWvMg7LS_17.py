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
  A=[x for x in beach]
  c=0
  if len(beach)==1 and beach=='0':
    c+=1
  else:
    if (A[0], A[1])==('0', '0'):
      A[0]='1'
      c+=1
    for i in range(1, len(A)-1):
      if (A[i-1], A[i], A[i+1])==('0', '0', '0'):
        A[i]='1'
        c+=1
    if (A[-2], A[-1])==('0', '0'):
      A[-1]='1'
      c+=1
  return c

