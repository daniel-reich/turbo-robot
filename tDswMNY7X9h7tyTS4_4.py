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

def pascal_row(n):
    if n < 2:
        return ([1], [1, 1])[n]
    len_res, n_plus_1 = (n + 2 - n % 2) // 2, n + 1
    res = [1] + [0] * (len_res - 1)
    for i in range(1, len_res):
        res[i] = res[i - 1] * (n_plus_1 - i) // i
    return res + res[::-1] if n % 2 else res + res[-2::-1]
​
def pascals_triangle(n):
    res = []
    for i in range(n):
        res += pascal_row(i)
    return res

