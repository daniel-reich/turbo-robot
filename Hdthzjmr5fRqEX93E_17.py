"""
Implement a function that returns a list containing all the consecutive
numbers in ascendant order from the given value `low` up to the given value
`high` (bounds included).

### Examples

    get_sequence(1, 5) ➞ [1, 2, 3, 4, 5]
    
    get_sequence(98, 100) ➞ [98, 99, 100]
    
    get_sequence(1000, 1000) ➞ [1000]

### Notes

  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're really stuck, unlock solutions in the **Solutions** tab.

"""

def get_sequence(low, high):
  
  List = []
  
  Value = low
  Ceiling = high
  
  while (Value <= Ceiling):
    List.append(Value)
    Value +=1
  
  return List

