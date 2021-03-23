"""


Create a function that takes a number `n` and returns the `n`th even number.

### Examples

    nth_even(1) ➞ 0
    # 0 is first even number
    
    nth_even(2) ➞ 2
    # 2 is second even number
    
    nth_even(100) ➞ 198

### Notes

N/A

"""

def nth_even(n):
# res = []
# for i in range(0,n):
#   if i % 2 == 0:
#     res += 1
# return res
  
  
  if n == 2:
    return 2
  elif n == 1:
    return 0
  return (n*2)-2

