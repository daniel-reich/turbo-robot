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

def football(s):
  ans = {i:0 for i in range(s+1)}
  ans[0] = 1
  
  for i in [2,3,6,7,8]:
    for a in sorted(ans.keys())[::-1]:
      ans[a] = sum(ans[a-r*i] for r in range(0,1+s//i) if a-r*i>=0)
  
  return ans[s]

