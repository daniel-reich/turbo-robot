"""


Write a function that sorts a given list in an aletrnative fashion. The result
should be a list sorted in ascending order (number then letter). Lists will
contain equal amounts of integer numbers and single characters.

### Examples

    alternate_sort(["a", "b", "c", 1, 2, 3]) ➞ [1, "a", 2, "b", 3, "c"]
    
    alternate_sort([-2, "f", "A", 0, 100, "z"]) ➞ [-2, "A", 0, "f", 100, "z"]
    
    alternate_sort(["X", 15, 12, 18, "Y", "Z"]) ➞ [12, "X", 15, "Y", 18, "Z"]

### Notes

N/A

"""

def alternate_sort(lst):
  
  Letters = []
  Numbers = []
  
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length):
    
    Type = type(lst[Counter])
    
    if (Type == int):
      Numbers.append(lst[Counter])
      Counter += 1
    
    elif (Type == str):
      Letters.append(lst[Counter])
      Counter += 1
    
    else:
      Counter += 1
  
  Numbers = sorted(Numbers)
  Letters = sorted(Letters)
  
  Combined = []
  Counter = 0
  Length = len(Letters)
  
  while (Counter < Length):
    Combined.append(Numbers[Counter])
    Combined.append(Letters[Counter])
    Counter += 1
  
  return Combined

