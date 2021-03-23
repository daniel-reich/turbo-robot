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
  count=0
  for i in range(10000000000):
    if not i%2:
      count+=1
      if count==n:
        return i

