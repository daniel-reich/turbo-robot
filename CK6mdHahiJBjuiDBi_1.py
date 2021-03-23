"""


You arrive at the supermarket checkout and you've only got a limited number of
shopping bags with you. Miser that you are, you hate buying extra bags when
you've got dozens at home that you forgot to bring with you!! Can you fit all
your shopping into the bags you've got with you?

Each bag can carry a maximum of 10kg and each item you've purchased weighs
between 1 and 10kg.

Create a function that takes two parameters, a list of the weights of each
item and the number of bags you are carrying. Return `True` if there are
enough bags to contain all the items, otherwise `False`.

### Example

    can_fit([2, 1, 2, 5, 4, 3, 6, 1, 1, 9, 3, 2], 4) ➞ True
    # Bag 1 = [2, 1, 2, 5] (10kg)
    # Bag 2 = [4, 3, 3] (10kg)
    # Bag 3 = [6, 2, 1, 1] (10kg)
    # Bag 4 = [9] (9kg)
    
    can_fit([2, 7, 1, 3, 3, 4, 7, 4, 1, 8, 2], 4) ➞ False
    # Bag 1 = [2, 8] (10kg)
    # Bag 2 = [3, 7] (10kg)
    # Bag 3 = [2, 4, 4] (10kg)
    # Bag 4 = [7, 3] (10kg)
    # two 1kg items left over!

### Notes

  * All weights will be integers between 1 and 10kg inclusive
  * Items can be packed in any order
  * There may be more than one way to fit all the items in the available bags

 ** _Based on an easier challenge[ How Many
Boxes?](https://edabit.com/challenge/QdEAMeXNJAivcTMiT) by @zatoichi49._**

"""

def can_fit(weights, bags):
  class Bag:
​
    def __init__(self, maxweight, ident, inventory = []):
      self.i = inventory
      self.w = 0
      self.id = ident
​
      for item in inventory:
        self.w += item.w
      
      self.mw = maxweight
      self.available = self.mw - self.w
​
    def add(self, item):
      if item.w <= self.available and item.b == None:
        self.i.append(item)
        self.w += item.w
        self.available = self.mw - self.w
        item.b = self.id
        return True
      else:
        return False
  class Item:
​
    def __init__(self, weight, bag = None):
      self.w = weight
      self.b = bag
​
  bag_dics = {}
​
  for n in range(1, bags + 1):
    bag_dics[n] = Bag(10, n)
  
  items_by_weight = {}
​
  for item in weights:
    if item not in items_by_weight.keys():
      items_by_weight[item] = [Item(item)]
    else:
      items_by_weight[item].append(Item(item))
  
  ibws = [item for lst in reversed(sorted(list(items_by_weight.keys()))) for item in items_by_weight[lst]]
​
  del items_by_weight
​
  for bag in bag_dics.values():
    for item in ibws:
      if item.b == None:
        t = bag.add(item)
​
  unbagged = [item for item in ibws if item.b == None]
​
  return len(unbagged) == 0

