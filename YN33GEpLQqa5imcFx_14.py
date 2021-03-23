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
    result = [1]
    bit = ""
    data = [[0 for i in range(row)] for j in range(row)]
    for i in range(row):
        data[0][i] = 1
        data[i][0] = 1
        
    for y in range(row - 1):
        for x in range(row - 1):
            data[y + 1][x + 1] = data[y + 1][x] + data[y][x + 1]
    for i in range(1, row):
        result.append(data[i][row - i])
    result.append(1)
    
    for i in result:
        bit += str(i) + " "
    return bit[ : - 1]

