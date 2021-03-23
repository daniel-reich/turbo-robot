"""


Create an ordered 2D list (matrix). A matrix is ordered if its (0, 0) element
is 1, its (0, 1) element is 2, and so on. Your function needs to create an a ×
b matrix. `a` is the first argument and `b` is the second.

### Examples

    ordered_matrix(5, 5) ➞ [
      [1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10],
      [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20],
      [21, 22, 23, 24, 25]
    ]
    
    ordered_matrix(1, 1) ➞ [[1]]
    
    ordered_matrix(1, 5) ➞ [[1, 2, 3, 4, 5]]

### Notes

  * `a` is the height of the matrix (y coordinate), and `b` is the width (x coordinate).
  * `a` and `b` will always be positive, and the matrix will always be square shaped (in each row are the same amount of columns).
  * `a` and `b` are integers.

"""

def ordered_matrix(height, width):
  matrix = []
  Neo = 0
  TAA = 0 #(Thomas A. Anderson)
  #Get it?
  Number = 1
  while(Neo < height):
    matrix.append([])
    Neo = Neo + 1
  Neo = 0
  while(Neo < height):
    while(TAA < width):
      matrix[Neo].append(Number)
      TAA = TAA + 1
      Number = Number + 1
    TAA = 0
    Neo = Neo + 1
  return(matrix)
  #Code By Cool Programmer

