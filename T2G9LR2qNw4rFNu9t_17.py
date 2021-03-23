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
  if size > len(array):
    return [array]
  else:
    newlist = []
    newlist2 = []
    for eachnumber in array:
      if len(newlist2) == size:
        newlist.append(newlist2)
        newlist2 = []
        newlist2.append(eachnumber)
      else:
        newlist2.append(eachnumber)
    newlist.append(newlist2)
    return newlist

