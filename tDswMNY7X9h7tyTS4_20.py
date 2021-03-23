"""


 **Mubashir** was reading about [Pascal's
triangle](https://en.wikipedia.org/wiki/Pascal's_triangle) on Wikipedia.

In mathematics, Pascal's triangle is a triangular array of the binomial
coefficients that arises in probability theory, combinatorics, and algebra.

![Mubashir](https://edabit-
challenges.s3.amazonaws.com/PascalTriangleAnimated2.gif)

Formula for Pascal's triangle is given by:

![Mubashir](https://edabit-challenges.s3.amazonaws.com/jbderjvbv.png)

where `n` denotes a row of the triangle, and `k` is the position of a term in
the row.

Create a function which takes a number `n` and returns **n top rows** of
Pascal's Triangle flattened into a one-dimensional list.

### Examples

    pascals_triangle(1) ➞ [1]
    
    pascals_triangle(2) ➞ [1, 1, 1]
    
    pascals_triangle(4) ➞ [1, 1, 1, 1, 2, 1, 1, 3, 3, 1]

### Notes

N/A

"""

pascal = [[1]]
line = [1, 1]
for _ in range(2, 50):
    new_line = [1]
    for i in range(1, len(line)):
        new_line.append(line[i - 1] + line[i])
    new_line.append(1)
    pascal.append(line[:])
    line = new_line[:]
​
def pascals_triangle(n):
    ans = []
    for i in range(n):
        ans += pascal[i]
    return ans

