"""


Create a function that returns the sum of all even elements in a 2D matrix.

### Examples

    sum_of_evens([
      [1, 0, 2],
      [5, 5, 7],
      [9, 4, 3]
    ]) ➞ 6
    
    // 2 + 4 = 6
    
    sum_of_evens([
      [1, 1],
      [1, 1]
    ]) ➞ 0
    
    sum_of_evens([
      [42, 9],
      [16, 8]
    ]) ➞ 66
    
    sum_of_evens([
      [],
      [],
      []
    ]) ➞ 0

### Notes

  * Submatrices will be of equal length.
  * Return 0 if the 2D matrix only consists of empty submatrices.

"""

def sum_of_evens(lst):
  total = 0 
  for series in lst:
    for ele in series:
      if not (ele % 2): total += ele
  return total

