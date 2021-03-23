"""


Write a method that accepts two integer parameters rows and cols. The output
is a 2d array of numbers displayed in column-major order, meaning the numbers
shown increase sequentially down each column and wrap to the top of the next
column to the right once the bottom of the current column is reached.

### Examples

    printGrid(3, 6) ➞ [
      [1, 4, 7, 10, 13, 16],
      [2, 5, 8, 11, 14, 17],
      [3, 6, 9, 12, 15, 18]
    ]
    
    printGrid(5, 3) ➞ [
      [1, 6, 11],
      [2, 7, 12],
      [3, 8, 13],
      [4, 9, 14],
      [5, 10, 15]
    ]
    
    printGrid(4, 1) ➞ [
      [1],
      [2],
      [3],
      [4]
    ]

### Notes

N/A

"""

def printgrid(rows, cols):
  return [[j+1 + i*rows for i in range(cols)] for j in range(rows)]

