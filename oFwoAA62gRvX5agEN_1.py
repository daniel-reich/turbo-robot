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

def knapsack(max_weight, items):   
    sorted_items = sorted(items, key = lambda item: item['value'], reverse = True)
    pruned_items = [item for item in sorted_items if item['weight'] <= max_weight]
    best_result = {
          'capacity': max_weight,
          'items': [],
          'weight': 0,
          'value': 0
    } 
    while pruned_items:
        item = pruned_items.pop()
        sub_results = knapsack(max_weight - item['weight'], pruned_items)
        sub_results['items'].append(item)
        sub_results['weight'] += item['weight']
        sub_results['value'] += item['value']
        sub_results['capacity'] = max_weight
        if sub_results['value'] > best_result['value']:
            best_result = sub_results
    #order matters to edabit
    best_result['items'] = sorted(best_result['items'], key = lambda item: items.index(item))
    return best_result

