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
  def combine(a, b): return a[0]+b[0], a[1]+b[1]
  def solve(cap, items):
    if cap<0: return (-float('inf'), [])
    if not items: return (0, [])
    return max(combine((items[0]['value'], [items[0]]),
                       solve(cap-items[0]['weight'], items[1:])),
               solve(cap, items[1:]),
               key=lambda x: x[0])
  _, chosen = solve(capacity, items)
  return {'capacity': capacity,
          'items': chosen,
          'weight': sum(x['weight'] for x in chosen),
          'value': sum(x['value'] for x in chosen)
  }

