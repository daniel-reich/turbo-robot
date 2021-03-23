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

class Pascals_Triangle:
  
  tri = [[1], [1, 1]]
  
  def advance_to(goal):
    while len(Pascals_Triangle.tri) < goal:
      prev_row = Pascals_Triangle.tri[-1]
      curr_row = [1]
      for n in range(len(prev_row) - 1):
        cn = prev_row[n]
        nn = prev_row[n+1]
        curr_row.append(cn + nn)
      curr_row.append(1)
      Pascals_Triangle.tri.append(curr_row)
    return True
  
  def display_to(n):
    return [i for lst in Pascals_Triangle.tri[:n] for i in lst]
​
Pascals_Triangle.advance_to(28)
​
def pascals_triangle(n):
  return Pascals_Triangle.display_to(n)

