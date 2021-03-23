"""


Create a function that multiplies two matrices (n x m) and (p x q) and
returns:

  * `"invalid"` if the matrices are not multiplicable (i.e. if m is not equal to p).
  * The multiplication matrix (n x q) otherwise.

### Examples

    matrix_multiply([[1, 2]], [[3], [4]]) ➞ [[11]]
    
    matrix_multiply([[0, 0], [0, 1]], [[1, 2], [3, 4], [5, 6]]) ➞ "invalid"
    
    matrix_multiply([[4, 2], [3, 1]], [[5, 6], [3, 8]]) ➞ [[26, 40], [18, 26]]

### Notes

This challenge is a generalized version of [Matrix
Multiplication](https://edabit.com/challenge/dfep4NR2twAFTdt9k).

"""

def matrix_multiply(a, b):
  rows , columns  = a, transpose(b);
  print(rows)
  print(columns)
  if (len(rows[0]) != len(columns[0])):
    return "invalid";
  return [[dot_prod(row , column) for column in columns] for row in rows ];
  
def dot_prod(row , other):
  return sum([a*b for a,b in zip(row , other)]);
  
def transpose(mtx):
  return [[row[colmn] for row in mtx ] for colmn in range(0,len(mtx[0])) ]

