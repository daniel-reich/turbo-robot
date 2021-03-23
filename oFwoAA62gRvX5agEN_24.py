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
  from itertools import combinations
  
  max_value, best_weight, best_group = 0, 0, list()
  
  for n in range(1, len(items)+1):
    for group in combinations(items, n):
      weights, values = 0, 0
      for item in group:
        weights += item["weight"]
        if weights > capacity:
          break
        values += item["value"]
      if values > max_value:
        max_value = values
        best_weight = weights
        best_group = group
  
  return {
    'capacity': capacity,
    'items': list(best_group),
    'weight': best_weight,
    'value': max_value
  }

