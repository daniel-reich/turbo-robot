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

def football(score):
  return sum(1 for a in range(score//2+1) for b in range(score//3+1) for c in range(score//6+1) for d in range(score//7+1) for e in range(score//8+1) if 2*a + 3*b + 6*c + 7*d + 8*e == score)
