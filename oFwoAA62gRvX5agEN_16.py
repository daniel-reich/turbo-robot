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
  def ks(n, c): 
    if n < 0 or c == 0:
      result = 0 
    elif items[n]['weight'] > c:
      result = ks(n-1, c)
    else:
      tmp1 = ks(n-1, c)
      tmp2 = items[n]['value'] + ks(n-1, c - items[n]['weight'])
      result = max(tmp2, tmp1)
    return result
​
  def lt(idx, cap, val):
    if val == 0 or cap == 0 or idx < 0:
      return []
    elif items[idx]['value'] > val:
      return lt(idx-1, cap, val)
    elif items[idx]['weight'] > cap:
      return lt(idx-1, cap, val)
    else:
      return min(lt(idx-1, cap, val), [items[idx]] + lt(idx-1, cap-items[idx]['weight'], val-items[idx]['value']), key = lambda x: val- sum(it['value'] for it in x))
​
  i = len(items)-1
  value = ks(i, capacity)
  items_list = lt(i, capacity, value)
  sorted_items_list = [item for item in items if item in items_list]
  weight = sum(item['weight'] for item in sorted_items_list)
  return {'capacity': capacity, 'items': sorted_items_list, 'weight': weight, 'value': value}

