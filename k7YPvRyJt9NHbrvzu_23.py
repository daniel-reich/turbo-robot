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
  flag=0
  i=0
  while i<=score//2:
    j=0
    while j<=score//3:
      k=0
      while k<=score//6:
        l=0
        while l<=score//7:
          m=0
          while m<=score//8:
            if 2*i+3*j+6*k+7*l+8*m == score:
              flag=flag+1
            m=m+1
          l=l+1
        k=k+1
      j=j+1
    i=i+1
  return flag

