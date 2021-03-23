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
  return max(products.keys(), key= lambda p: products[p])

