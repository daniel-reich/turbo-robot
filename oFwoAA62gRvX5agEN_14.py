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

import random
def knapsack(capacity, items):
    finaldict = {}
    finaldict['capacity'] = capacity
    finaldict['weight'] = 0
    finaldict['value'] = 0
    finaldict['items'] = []
    highest = 0
    best_weight = 0
    best_value = 0
    best_combo = [{}]
    finalfinaldict = {}
    finalfinaldict['capacity'] = capacity
    finalfinaldict['weight'] = 0
    finalfinaldict['value'] = 0
    finalfinaldict['items'] = []
    
    if capacity == 0:
        return finaldict
    
    for _ in range(50000):
        x = random.sample(items, random.randint(1,len(items)))
        weight = sum(item['weight'] for item in x)
        value = sum(item['value'] for item in x)
        
        if weight <= capacity:
            if value > highest:
                best_combo = x
                highest = value
                best_weight = weight
                best_value = value
    
    finaldict['items'].append(best_combo)
    finaldict['weight'] = best_weight
    finaldict['value'] = best_value
    
    finaldict['items'] = finaldict['items'][0]
    for i in items:
        if i in finaldict['items']:
            finalfinaldict['items'].append(i)
            
    finalfinaldict['weight'] = best_weight
    finalfinaldict['value'] = best_value
    return finalfinaldict

