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
  if capacity == 0:
      return {'capacity':0, 'items':[], 'weight':0, 'value':0}
  value = {}
  for weight in range(1, capacity+1):
      for item in items:
          diff = weight - item['weight']
          if diff == 0:
              if item['value'] > value.get(weight, {}).get('value', 0):
                  value[weight] = {'items':[item], 'value':item['value']}
          elif diff in value:
              prev = value[diff]['items']
              val = value[diff]['value']
              if item in prev:
                  continue
              if item['value'] + val > value.get(weight, {}).get('value', 0):
                  value[weight] = {'items':prev + [item], 'value': val + item['value']}
  cap = max(value, key=lambda x:value[x]['value'])
  res = {'weight': cap, 'value':value[cap]['value'], 'capacity': capacity}
  res['items'] = sorted(value[cap]['items'], key=items.index)
  return res

