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
  if n%2:
    x=(n-1)//2
    return n*(1+4*(x*(x+1)//2))
  return (1+n**2)*(n//2)
