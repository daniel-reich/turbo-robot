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

def knapsack(capacity, items):
  max_value = -float('inf')
  d = {'capacity': capacity, 'items': [], 'weight': 0, 'value': 0}
  for i in range(2**len(items)):
    items_ = [x for x, b in zip(items, format(i, '#0{}b'.format(len(items)+2))[2:]) if b=='1']
    w = sum(x['weight'] for x in items_)
    if w > capacity: continue
    v = sum(x['value'] for x in items_)
    if max_value < v:
      max_value = v
      d.update({'items': items_, 'weight': w, 'value': v})
  return d

