"""


An **almost-sorted sequence** is a sequence that is **strictly increasing** or
**strictly decreasing** if you remove a **single element** from the list (no
more, no less). Write a function that returns `True` if a list is **almost-
sorted** , and `False` otherwise.

For example, if you remove `80` from the first example, it is perfectly sorted
in ascending order. Similarly, if you remove `7` from the second example, it
is perfectly sorted in descending order.

### Examples

    almost_sorted([1, 3, 5, 9, 11, 80, 15, 33, 37, 41] ) ➞ True
    
    almost_sorted([6, 5, 4, 7, 3]) ➞ True
    
    almost_sorted([6, 4, 2, 0]) ➞ False
    // Sequence is already sorted.
    
    almost_sorted([7, 8, 9, 3, 10, 11, 12, 2]) ➞ False
    // Requires removal of more than 1 item.

### Notes

  * Completely sorted lists should return `False`.
  * Lists will always be **> 3** in length (to remove ambiguity).
  * Numbers in each input list will be unique - don't worry about "ties".

"""

def almost_sorted(lst):
  
  Original = lst
  
  Forward = sorted(Original)
  Backward = sorted(Original, reverse=True)
    
  if (Original == Forward) or (Original == Backward):
    return False
    
  Counter = 0
  Length = len(Original)
  
  while (Counter < Length):
        
    Exhibit = []
        
    Cursor = 0
    Span = len(Original)
        
    while (Cursor < Span):
      Item = Original[Cursor]
            
      if (Cursor == Counter):
        Cursor += 1
      else:
        Exhibit.append(Item)
        Cursor += 1
        
    Sample_A = sorted(Exhibit)
    Sample_B = sorted(Exhibit, reverse=True)
        
    if (Exhibit == Sample_A) or (Exhibit == Sample_B):
      return True
    else:
      Counter += 1
  
  return False

