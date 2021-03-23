"""


You call your spouse to inform his/her most precious item is gone! Given a
dictionary of stolen items, return the most expensive item on the items.

### Examples

    most_expensive_item({
      "piano": 2000,
    }) ➞ "piano"
    
    most_expensive_item({
      "tv": 30,
      "skate": 20,
    }) ➞ "tv"
    
    most_expensive_item({
      "tv": 30,
      "skate": 20,
      "stereo": 50,
    }) ➞ "stereo"

### Notes

  * There will only be one most valuable item ( _no ties_ ).
  * The dictionary will always contain at least one item ( _no empty dictionary_ ).

"""

def most_expensive_item(products):
  
  Things = []
  
  for x in products.keys():
    Things.append(x)
  
  Worth = []
  
  for y in products.values():
    Worth.append(y)
    
  Highest = max(Worth)
  
  Counter = 0
  Length = len(Things)
  
  while (Counter < Length):
    Item = Things[Counter]
    Money = Worth[Counter]
    
    if (Money == Highest):
      return Item
    else:
      Counter += 1

