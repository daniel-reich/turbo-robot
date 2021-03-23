"""


Given a knapsack with a certain weight capacity, fill it with loot from a list
of items to achieve the highest value possible.

The function takes two parameters: an integer specifying the maximum weight
the knapsack can hold, and a list of dictionary items to choose from. Each
item has a name, a weight, and a value. The total weight of all chosen items
cannot exceed the capacity of the knapsack.

The function should return a dictionary containing the capacity of the bag, a
list of items that were added to the bag (in the same order that they were
given), the total weight of those items, and the total value of the items.

### Example

    knapsack(0, items) ➞ {
      "capacity": 0,
      "items": [],
      "weight": 0,
      "value": 0
    }

### Notes

N/A

"""

from itertools import permutations as p
​
class Thing:
  def __init__(self, name, weight, value):
    self.name = name
    self.weight = weight
    self.value = value
​
  def display_info(self):
    print(self.name, self.weight, self.value)
​
def knapsack(capacity, items):
  things = []
  for x in items:
    v = x['value']
    w = x['weight']
    n = x['name']
    things.append(Thing(n, w, v))
    
  combos = p(things)
  print(list(combos))

