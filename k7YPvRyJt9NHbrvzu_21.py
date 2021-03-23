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
  out = 0
  for i in range(1 + score//2):
    for j in range(1 + score//3):
      for k in range(1 + score//6):
        for l in range(1 + score//7):
          for m in range(1 + score//8):
            if score == i*2 + j*3 + k*6 + l*7 + m*8:
              out+=1
  return out

