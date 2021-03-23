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
  ans=[]
  a=[]
  for i in array:
    a.append(i)
    if len(a)==size:
      ans.append(a)
      a=[]
  if a: ans.append(a)
  return ans

