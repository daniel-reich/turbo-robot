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
  dpCache = {(0,-1):(0, [])}
  def dp_knapsack(cap, itmIdx):
    if (cap, itmIdx) in dpCache:
      return dpCache[(cap, itmIdx)]
    elif cap < 0 or itmIdx < 0:
      return None
    
    options = [dp_knapsack(cap, itmIdx - 1), 
              dp_knapsack(cap - 1, itmIdx)]   
    temp = dp_knapsack(cap - items[itmIdx]['weight'], itmIdx -1)
    if temp is not None:
      options.append((temp[0] + items[itmIdx]['value'], temp[1][:] + [itmIdx]))
    options = filter(lambda x: x is not None, options)
    
    choice = max(options, key=lambda x:x[0])
    dpCache[(cap, itmIdx)] = choice
    return choice
    
  optimal = dp_knapsack(capacity, len(items) - 1)
  out = {"capacity":capacity, "items":[], "weight":0, "value":optimal[0]}
  for idx in optimal[1]:
    out["items"].append(items[idx])
    out["weight"] += items[idx]["weight"]
  print(dpCache)
  return out

