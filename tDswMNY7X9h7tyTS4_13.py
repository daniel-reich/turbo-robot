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

def fac(n):
  if n == 0:
    return 1
  else:
    return n * fac(n-1)
​
def arr_pas(n):
    arr_res = []
    for i in range(n+1):
        item = fac(n)/(fac(i)*fac(n-i))
        arr_res.append(int(item))
    return arr_res
  
def pascals_triangle(n):
  arr_res = []
  for i in range(n):
    arr_res += arr_pas(i)
  return arr_res

