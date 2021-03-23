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
  
  Answer = []
  
  Counter = 0
  Length = len(array)
  
  while (Counter < Length):
  
    Batch = []
    Added = 0
    Required = size
    
    while (Added < Required) and (Counter < Length):
      Item = array[Counter]
      Batch.append(Item)
      Added += 1
      Counter += 1
    
    Answer.append(Batch)
    
  return Answer

