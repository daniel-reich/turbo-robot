"""


Create a function that takes two lists and combines them by alternatingly
taking elements from each list in turn.

  * The lists may be of different lengths, with at least one character / digit.
  * The first list will contain string characters (lowercase, a-z).
  * The second list will contain integers (all positive).

### Examples

    merge_arrays(["a", "b", "c", "d", "e"], [1, 2, 3, 4, 5])
    ➞ ["a", 1, "b", 2, "c", 3, "d", 4, "e", 5]
    
    merge_arrays([1, 2, 3], ["a", "b", "c", "d", "e", "f"])
    ➞ [1, "a", 2, "b", 3, "c", "d", "e", "f"]
    
    merge_arrays(["f", "d", "w", "t"], [5, 3, 7, 8])
    ➞ ["f", 5, "d", 3, "w", 7, "t", 8]

### Notes

N/A

"""

def merge_arrays(a, b):
​
  List_A = a
  List_B = b
  
  Length_A = len(List_A)
  Length_B = len(List_B)
  Shortest = min(Length_A,Length_B)
  
  Answer = []
  
  Cursor = 0
  End = len(List_A)
  
  while (Cursor < Shortest):
    
    Item_A = List_A[Cursor]
    Item_B = List_B[Cursor]
    
    Answer.append(Item_A)
    Answer.append(Item_B)
    
    Cursor += 1
​
  Test_A = Length_A + Length_B
  Test_B = len(Answer)
  Longest = max(Length_A,Length_B)
  
  if (Test_A == Test_B):
    return Answer
  
  else:
    
    while (Cursor < Longest):
​
      if (Length_A == Longest):
        Item = List_A[Cursor]
        Answer.append(Item)
        Cursor += 1
​
      elif (Length_B == Longest):
        Item = List_B[Cursor]
        Answer.append(Item)
        Cursor += 1
​
      else:
        Cursor += 1
​
  return Answer

