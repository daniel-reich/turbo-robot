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
  out = []
  while len(lst) > size:
    out.append(lst[:size])
    lst = lst[size:]
  out.append(lst)
  return out

