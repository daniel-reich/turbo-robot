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

def count(lst,score,n):
  if score == 0:
    return 1
  elif score < 0:
    return 0
  elif n <= 0 and score > 0:
    return 0
  else:
    return count(lst,score,n-1) + count(lst, score - lst[n-1], n)
​
def football(score):
  return count([2,3,6,7,8],score,5)

