"""


The function is given a non-negative integer `n`. Determine if there exist two
non-negative integers `a` and `b` such that `a**2 + b**2 == n`, return `True`
/ `False`.

### Examples

    squares_sum(0) ➞ True
    # 0^2 + 0^2 == 0
    
    squares_sum(1) ➞ True
    # 0^2 + 1^2 == 1
    
    squares_sum(2) ➞ True
    # 1^2 + 1^2 == 2
    
    squares_sum(3) ➞ False
    # Checking 0, 1 we can’t make the sum of squares equal to 3.
    
    squares_sum(5) ➞ True
    # 1^2 + 2^2 == 5

### Notes

The input range is `0 <= n < 2**31`.

"""

def squares_sum(n):
  return any(
    (n - k ** 2) ** 0.5 % 1 == 0
    for k in range(int(n ** 0.5) + 1)
  )

