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
  if (by_value(capacity, items)["value"] > by_value_per_weight(capacity, items)["value"]):
    return by_value(capacity, items)
  return by_value_per_weight(capacity, items)
  
def by_value(capacity, items):
  sorted_items = sorted(items, key=lambda k: k['value'])
  weight = 0  
  looted_items = []
  while (weight < capacity):
    if (len(sorted_items) == 0):
      break
    item = sorted_items.pop()
    if ((item["weight"] + weight) <= capacity):
      looted_items.append(item) 
      weight += item["weight"]
  final_items = [x for x in items if x in looted_items]
  value = sum(item["value"] for item in looted_items)
  return {
    "capacity": capacity,
    "items": final_items,
    "weight": weight,
    "value": value
  }
​
def by_value_per_weight(capacity, items):
  sorted_items = sorted(items, key=lambda k: k['value']/k["weight"])
  weight = 0  
  looted_items = []
  while (weight < capacity):
    if (len(sorted_items) == 0):
      break
    item = sorted_items.pop()
    if ((item["weight"] + weight) <= capacity):
      looted_items.append(item) 
      weight += item["weight"]
  final_items = [x for x in items if x in looted_items]
  value = sum(item["value"] for item in looted_items)
  return {
    "capacity": capacity,
    "items": final_items,
    "weight": weight,
    "value": value
  }

