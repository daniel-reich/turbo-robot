"""


Imagine this triangle:

        1
       2 3
      4 5 6
     7 8 9 10
    ...

Create a function that takes a number `n` and returns the sum of all numbers
in **nth row**.

### Examples

    row_sum(1) ➞ 1
    
    row_sum(2) ➞ 5
    
    row_sum(4) ➞ 34

### Notes

1 <= N <= 1000

"""

def row_sum(n):
  quad = lambda x: int(0.5 * x * x - 0.5 * x + 1)
  return sum(range(quad(n), quad(n + 1)))

