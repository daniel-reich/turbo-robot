"""


Create a function that takes a number `n` and returns the _sum_ of all square
numbers up to and including `n`.

    squares_sum(3) ➞ 14
    # 1² + 2² + 3² =
    # 1 + 4 + 9 =
    # 14

### Examples

    squares_sum(3) ➞ 14
    
    squares_sum(12) ➞ 650
    
    squares_sum(13) ➞ 819

### Notes

Remember that `n` is included in the total.

"""

def squares_sum(n):
  return sum([x**2 for x in range(1, n+1)])

