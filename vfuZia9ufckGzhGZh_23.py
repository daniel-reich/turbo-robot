"""


Create a function that determines if a given sequence is _linear_ ,
_quadratic_ or _cubic_. The input will be a list of numbers of varying
lengths. The function should return `"Linear"`, `"Quadratic"` or `"Cubic"`.

### Examples

    seq_level(1, 2, 3, 4, 5) ➞ "Linear"
    
    seq_level(3, 6, 10, 15, 21) ➞ "Quadratic"
    
    seq_level(4, 14, 40, 88, 164) ➞ "Cubic"

### Notes

N/A

"""

def seq_level(lst):
  
  # Establishing First Layer of Differences
  
  Draft_One = []
  
  First = 0
  Second = 1
  Length = len(lst)
  
  while (Second < Length):
    Item_A = lst[Second]
    Item_B = lst[First]
    Difference = Item_A - Item_B
    Draft_One.append(Difference)
    First += 1
    Second += 1
  
  # Establishing Second Layer of Differences
  
  Draft_Two = []
  
  First = 0
  Second = 1
  Length = len(Draft_One)
  
  while (Second < Length):
    Item_A = Draft_One[Second]
    Item_B = Draft_One[First]
    Difference = Item_A - Item_B
    Draft_Two.append(Difference)
    First += 1
    Second += 1
  
  # Establishing Third Layer of Differences
  
  Draft_Three = []
  
  First = 0
  Second = 1
  Length = len(Draft_Two)
  
  while (Second < Length):
    Item_A = Draft_Two[Second]
    Item_B = Draft_Two[First]
    Difference = Item_A - Item_B
    Draft_Three.append(Difference)
    First += 1
    Second += 1
  
  # Establishing Where Constant Difference Exists
  
  Unique_A = set(Draft_One)
  Unique_A = list(Unique_A)
  Test_A = len(Unique_A)
  
  Unique_B = set(Draft_Two)
  Unique_B = list(Unique_B)
  Test_B = len(Unique_B)
  
  Unique_C = set(Draft_Three)
  Unique_C = list(Unique_C)
  Test_C = len(Unique_C)
  
  # Establishing Answer
​
  if (Test_A == 1):
    return "Linear"
  
  elif (Test_B == 1):
    return "Quadratic"
  
  elif (Test_C == 1):
    return "Cubic"
  
  else:
    return "More Complicated"

