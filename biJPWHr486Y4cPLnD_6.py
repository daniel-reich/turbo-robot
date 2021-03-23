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
  if len(lst)<size:
    return [lst]
  if len(lst)%size!=0:
    m=size-len(lst)%size
    for i in range(m):
      lst.append(' ')
  result=[]
  for y in range(len(lst)//size):
    for x in range(size):
      if x == 0:
        result.append([])
      result[y].append(lst[x+y*size])
  if result[-1][-1]==' ':
    for i in range(m):
      result[-1].pop()
  return result

