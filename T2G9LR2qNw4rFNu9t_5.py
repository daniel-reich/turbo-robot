"""


Given a list and chunk size "n", create a function such that it divides the
list into many sublists where each sublist is of length size "n".

### Examples

    chunk([1, 2, 3, 4], 2) ➞ [
      [1, 2], [3, 4]
    ]
    
    chunk([1, 2, 3, 4, 5, 6, 7], 3) ➞ [
      [1, 2, 3], [4, 5, 6], [7]
    ]
    
    chunk([1, 2, 3, 4 ,5], 10) ➞ [
      [1, 2, 3, 4, 5]
    ]

### Notes

Remember that number of sublists may not be equal to chunk size.

"""

def chunk(array, size):
  
  chunks = []
  l = []
  c = 0
  
  while c < len(array):
    if len(l) == size:
      chunks.append(l)
      l = []
    l.append(array[c])
    c += 1
  
  if len(l) > 0:
    chunks.append(l)
  
  del l
  
  return chunks

