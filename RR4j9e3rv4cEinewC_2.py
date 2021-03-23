"""


This fabled hat company has 5 production lines running simultaneously. The
speed of each production line varies depending on the style and quality of the
hat being produced. You will be given the number of hats required and a list
of production line speeds.

Your job is to devise a function that will find the number of minutes elapsed
for exactly `n` hats to be finished. If exactly `n` hats cannot be made in any
time frame, return `None`. The speeds given are the number of minutes required
to make one hat.

### Examples

    hats([5, [1, 1, 1, 1, 1]]) ➞ "1 minute"
    # If each line makes a hat in 1 min, it takes 1 min to make 5 hats.
    
    hats([3, [23, 11, 19, 9, 36]]) ➞ "18 minutes"
    
    hats([650, [23, 11, 19, 9, 36]]) ➞ "2001 minutes"
    
    hats([9, [23, 11, 19, 9, 36]]) ➞ None

### Notes

N/A

"""

from fractions import gcd
from functools import reduce
​
def lcm(*args):
    return reduce(lambda x, y: y * x // gcd(x, y), args)
​
def hats(lst):
  n, m = lst
  sch = m[:]
  minsPerCycle = lcm(*m)
  hatsPerCycle = sum(minsPerCycle // m[i] for i in range(len(m)))
  cycles, toMake = divmod(n, hatsPerCycle)
  made = cycles * hatsPerCycle
  mins = 0
  while made < n:
    i = sch.index(min(sch))
    mins = sch[i]
    for i in range(len(sch)):
      if (sch[i] == mins):
        made += 1
        sch[i] += m[i]
  mins += minsPerCycle * cycles
  return "{} minute{}".format(mins, 's' if mins > 1 else '') if made == n else None

