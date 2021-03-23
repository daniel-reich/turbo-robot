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

#adapted from Vitosh Academy
#https://www.vitoshacademy.com/python-algorithms-maximum-combinations-of-coins/
def football(score):
  points = (0,2,3,6,7,8)
  p = [0]*(score+1)
  for point in points:
      for i in range(score+1):
          if point == i:
              p[i]+=1
          if i-point>0:
              p[i]=p[i]+p[i-point]
  return p[score]

