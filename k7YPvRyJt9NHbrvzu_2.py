"""


Scoring plays in American football count as either 2, 3, 6, 7, or 8 points.
Write a function that has as it's argument a football score and returns the
number of possible ways that score can be achieved. Order is not important.

### Examples

    football(4) ➞ 1
    # 2+2
    
    football(6) ➞ 3
    # 2+2+2 or 3+3 or 6
    
    football(7) ➞ 2
    # 2+2+3 or 7
    
    football(9) ➞ 4
    # 2+2+2+3 or 3+3+3 or 3+6 or 7+2

### Notes

N/A

"""

from itertools import combinations_with_replacement
def football(score):
  scores,counter,iterr=[2, 3, 6, 7, 8],0,0
  while (iterr < score//min(scores)+1):
    for e in set(list(combinations_with_replacement(scores,iterr))):
      if sum(e)==score:
        counter+=1
    iterr+=1
  return counter

