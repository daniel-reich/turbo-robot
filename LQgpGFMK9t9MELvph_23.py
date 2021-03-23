"""


Given a square list ( _n_ * _n_ size) implement a function that returns a new
list containing two lists equal to the two diagonals, in the following order:

    diagonal 1 = from upper-left to lower-right corner
    diagonal 2 = from upper-right to lower-left corner

### Examples

    get_diagonals([ [1, 2], [3, 4] ]) ➞ [ [1, 4], [2, 3] ]
    
    get_diagonals([ ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"] ]) ➞ [ ["a", "e", "i"], ["c", "e", "g"] ]
    
    get_diagonals([ [True] ]) ➞ [ [True], [True] ]

### Notes

  * Your function must also work with single elements or empty lists.
  * Try to build both diagonals with a single loop.

"""

def get_diagonals(lst):
  
  if (lst == []):
    return [[],[]]
  
  Length = len(lst)
  
  if (Length == 1):
    Answer = []
    Answer.append(lst[0])
    Answer.append(lst[0])
    return Answer
  
  if (Length == 2):
    return lst
  
  # Assuming Length is Greater Than Two
  # Bucket for Final Answer
  
  Answer = []
  
  # Going Top Left to Bottom Right
  
  Batch = []
  
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length): 
    Item = lst[Counter][Counter]
    Batch.append(Item)
    Counter += 1
  
  Answer.append(Batch)
  
  # Going Top Right to Bottom Left
  
  Batch = []
  
  Counter = 0
  Cursor = -1
  Length = len(lst)
  End = Length * -1
  
  while (Counter < Length):
    Item = lst[Counter][Cursor]
    Batch.append(Item)
    Counter += 1
    Cursor -= 1
  
  Answer.append(Batch)
  
  # Giving Answer
  return Answer

