"""


Write a function that replaces each integer with the next largest in the list.

### Examples

    replace_next_largest([5, 7, 3, 2, 8]) ➞ [7, 8, 5, 3, -1]
    
    replace_next_largest([2, 3, 4, 5]) ➞ [3, 4, 5, -1]
    
    replace_next_largest([1, 0, -1, 8, -72]) ➞ [8, 1, 0, -1, -1]

### Notes

  * Replace the maximum with **-1**.
  * Elements in the list will be unique.
  * You don't have to swap the elements.

"""

def replace_next_largest(lst):
  
  Sample = lst
  Maximum = max(Sample)
  Sorted = sorted(Sample)
  
  Revised = []
  
  Counter = 0
  Length = len(Sample)
  
  while (Counter < Length):
    
    Item = Sample[Counter]
    
    if (Item == Maximum):
      Revised.append(-1)
      Counter += 1
    
    else:
      Cursor = 0
      Span = len(Sample)
    
      while (Cursor < Span):
        
        Item_A = Sample[Counter]
        Item_B = Sorted[Cursor]
        
        if (Item_A >= Item_B):
          Cursor += 1
        else:
          Revised.append(Item_B)
          Cursor += Span
      
      Counter += 1
  
  return Revised

