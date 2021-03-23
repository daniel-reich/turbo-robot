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

from itertools import permutations
​
def knapsack(capacity, items):
  permutation_list = []
  best_item_list = []
  best_weight = 0
  best_value = 0
  content_dict = {'capacity': 0, 'items': [], 'weight': 0, 'value': 0}
  sample_item = {'name': "", 'weight': 0, 'value': 0}
  if capacity == 0:
    return content_dict
  for r in range(1,len(items)+1):
    permutation_list.extend(list(permutations(items,r)))
  print(permutation_list)
  for item_list in permutation_list:
    sum_weight = 0
    sum_value = 0
    for item in item_list:
      sum_weight += item.get('weight')
      sum_value += item.get('value')
    if sum_weight <= capacity and sum_value > best_value:
      best_item_list = item_list[:]
      best_value = sum_value[:]
      best_weight = sum_weight[:]
  content_dict = {'capacity': capacity, 'items': best_item_list, 'weight': best_weight, 'value': best_value}
  return(content_dict)

