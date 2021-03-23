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
    
def knapsack(capacity, items):
    if capacity == 0: return {'value': 0, 'weight': 0, 'items': [], 'capacity': 0}
    itemcount = []
    j = 0
    numbereditems = []
    for item in items:
        numbereditems.append((j,item["name"],item["weight"],item["value"]))
        itemcount.append(j)
        j += 1
    
    bestcomb = []
    maxv = bestv = bestw = 0
    for i in range(1,len(itemcount)+1):
        combs = combinations(itemcount, i)
        for comb in list(combs):
            combw = combv= 0
            for num in comb:
                combw += numbereditems[num][2]
                combv += numbereditems[num][3]
            if combw <= capacity and combv > maxv:
                bestcomb = sorted(comb)
                maxv = combv
                bestw = combw
​
    bestitem = {}
    bestitemslist = []
    for num in bestcomb:
        bestitem = {'name': numbereditems[num][1],'weight': numbereditems[num][2],'value': numbereditems[num][3]}
        bestitemslist.append(bestitem)
    
    returnobj = {"capacity":capacity,"items":bestitemslist,"weight":bestw,"value":maxv}
    return returnobj

