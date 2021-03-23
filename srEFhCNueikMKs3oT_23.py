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
  return ((n&(n-1)) and n) == n

