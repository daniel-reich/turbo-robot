"""


Write a function that divides a list into chunks of size **n** , where **n**
is the length of each chunk.

### Examples

    chunkify([2, 3, 4, 5], 2) ➞ [[2, 3], [4, 5]]
    
    chunkify([2, 3, 4, 5, 6], 2) ➞ [[2, 3], [4, 5], [6]]
    
    chunkify([2, 3, 4, 5, 6, 7], 3) ➞ [[2, 3, 4], [5, 6, 7]]
    
    chunkify([2, 3, 4, 5, 6, 7], 1) ➞ [[2], [3], [4], [5], [6], [7]]
    
    chunkify([2, 3, 4, 5, 6, 7], 7) ➞ [[2, 3, 4, 5, 6, 7]]

### Notes

  * It's O.K. if the last chunk is not completely filled (see example #2).
  * Integers will always be single-digit.

"""

def chunkify(lst, size):
  a = len(lst) // size
  b = len(lst) % size
  x = []
  for i in range(0, len(lst)-b,size):
    x.append(lst[i:i+size])
  if b != 0:
    x.append(lst[len(lst)-b:])
  return x

