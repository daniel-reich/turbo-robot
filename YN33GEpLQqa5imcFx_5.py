"""


The goal of this challenge is to return Pascal's triangle up to number 29.
Pascal's triangle is the sum of the two upper corners.

       1 1
      1 2 1
     1 3 3 1
    
    # There will always be the 1 in the first
    # place and the row in the second.

![Pascal's Triangle](https://edabit-
challenges.s3.amazonaws.com/PascalTriangleAnimated2.gif)

Create a function that returns a row from Pascal's triangle. To find the row
and column you can use `n!/(k!*(n-k)!)` where `n` is the row down and `k` is
the column.

### Examples

    pascals_triangle(1) ➞ "1 1"
    
    pascals_triangle(4) ➞ "1 4 6 4 1"
    
    pascals_triangle(6) ➞ "1 6 15 20 15 6 1"
    
    pascals_triangle(8) ➞ "1 8 28 56 70 56 28 8 1"

### Notes

N/A

"""

def pascals_triangle(row):
  p = [0,1,0]
  for _ in range(row):
    p = [0] + [sum(z) for z in zip(p,p[1:])] + [0]
  return ' '.join(map(str,p[1:-1]))

