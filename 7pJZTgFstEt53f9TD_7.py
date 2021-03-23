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

def transpose_matrix(lst):
  x = lst
  if len(x) != 0:
    dim = (len(x[0]),len(x))
  else:
    dim = (0,0)
​
  out = []
​
  for i in range(0,dim[0]):
    out.append([])
​
  for i in range(0,len(x)):
    for k,v in enumerate(x[i]):
      out[k].append(v)
      
  return out

