"""


Write a function that accepts an integer `n` and returns an `n * n` spiral
matrix.

### Examples

    matrix(2) ➞ [
      [1, 2],
      [4, 3]
    ]
    
    matrix(3) ➞ [
      [1, 2, 3],
      [8, 9, 4],
      [7, 6, 5]
    ]
    
    matrix(4) ➞ [
      [1,  2,  3,  4],
      [12, 13, 14, 5],
      [11, 16, 15, 6],
      [10,  9,  8, 7]
    ]

### Notes

In the examples, traverse the matrix in the clock-wise direction to observe
the spiral pattern.

"""

def trans(lst):
  return list(zip(*lst))[::-1]
def matrix(n):
  A=[x for x in range(1, n**2+1)]
  lst=[A[i:i+n] for i in range(0, len(A), n)]
  lst2=[]
  while lst:
    lst2+=lst.pop(0)
    lst=trans(lst)
  B=sorted([x for x in zip(A,lst2)], key=lambda x:x[1])
  C=[x[0] for x in B]
  res=[C[i:i+n] for i in range(0, len(C), n)]
  return res

