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
  
  answer = []
  start = 1
  
  rows_added = 0
  rows_required = rows
  
  while (rows_added < rows_required):
  
    batch = []
    value = start
    columns_added = 0
    columns_required = cols
    
    while (columns_added < columns_required):
      batch.append(value)
      value += rows
      columns_added += 1
    
    answer.append(batch)
    start += 1
    rows_added += 1
  
  return answer

