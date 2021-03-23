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
  import copy
  matrix = []
  ordered_names = [item['name'] for item in items]
  values = copy.copy(items)
  values.sort(key=lambda x: (x['weight'], x['value']))
  for _ in range(len(values)):
    l = [0] * (capacity + 1)
    matrix.append(l)
​
  # algorithm starts because we have a 2d array
  # x coordinate are the weights and y are the items
  for y, row in enumerate(matrix):
    item = values[y]
    value = item['value']
    weight = item['weight']
    for x, column in enumerate(row):
      if x < 1:
        continue
      above_value = matrix[y - 1][x] if y else 0
      other_items =  matrix[y - 1][x - weight] if y - 1 >= 0 and x - weight >= 0 else 0
      matrix[y][x] = max(value + other_items, above_value)
​
  # traverse results to get the items that were selected
  y = len(matrix) - 1
  x = len(matrix[0]) - 1
  names = []
  while x >= 0 and y >= 0:
    if not matrix[y][x]:
      break
    if matrix[y][x] == matrix[y - 1][x]:
      y -= 1
      continue
    item = values[y]
    names.append(item['name'])
    y -= 1
    x -= item['weight']
  selected_items = []
  for name in ordered_names:
    if name in names:
      for item in values:
        if item['name'] == name:
          selected_items.append(item)
  total_weight = sum([item['weight'] for item in selected_items])
  value = sum([item['value'] for item in selected_items])
​
  return {'capacity': capacity, 'items': selected_items,
          'weight': total_weight, 'value': value}

