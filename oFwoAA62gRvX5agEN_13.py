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

from itertools import combinations
def knapsack(size, items):
    max_value = 0
    # discard items if their weight is greater than limit
    items = [item for item in items if item["weight"] <= size]
    indices = range(len(items))
    best_indices=[]
    for n in indices:
        for i in combinations(indices, n+1):
            total_value = sum(items[p]["value"] for p in i)
            total_weight = sum(items[p]["weight"] for p in i)
            if total_value > max_value and total_weight <= size:
                max_value = total_value
                best_indices = i
    bag = [items[index] for index in best_indices]
    return {
        'capacity': size,
        'items': bag,
        'weight': sum(item["weight"] for item in bag),
        'value': sum(item["value"] for item in bag)
        }

