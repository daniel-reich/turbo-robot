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

def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n >= 2:
        return n*factorial(n-1)
​
def pascals_triangle(n):
    row_as_list = []
    for k in range(n+1):
        number = factorial(n) / (factorial(k)*factorial(n-k))
        row_as_list.append(str(int(number)))
    row_as_string = " ".join(row_as_list)
    return row_as_string

