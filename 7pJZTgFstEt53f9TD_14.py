"""


Create a function that transposes a 2D matrix.

### Examples

    transpose_matrix([
      [1, 1, 1],
      [2, 2, 2],
      [3, 3, 3]
    ]) ➞ [
      [1, 2, 3],
      [1, 2, 3],
      [1, 2, 3]
    ]
    
    transpose_matrix([
      [5, 5],
      [6, 7],
      [9, 1]
    ]) ➞ [
      [5, 6, 9],
      [5, 7, 1]
    ]

### Notes

N/A

"""

def transpose_matrix(array):
​
  res = [] 
​
  for i in range(len(array[0])):
    temp = [] 
    for j in range(len(array)):
      temp.append(array[j][i])
    res.append(temp)
​
  return(res)

