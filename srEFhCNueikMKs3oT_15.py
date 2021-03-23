"""


Create a function that takes a number `n` as an argument and checks whether
the given number can be expressed as a sum of **two or more consecutive
positive numbers**.

### Examples

    consecutiveSum(9) ➞ True
    # 9 can be expressed as a sum of (2 + 3 + 4) or (4 + 5).
    
    consecutiveSum(10) ➞ True
    # 10 can be expressed as a sum of 1 + 2 + 3 + 4.
    
    consecutiveSum(64) ➞ False

### Notes

N/A

"""

def consecutive_sum(n):
  lst = list(range(1,n//2+2))
  for i in range(len(lst)):
    szum = 0
    for j in range(i,len(lst)):
      szum += lst[j]
      if szum == n:
        return True
      if szum > n:
        break
  return False

