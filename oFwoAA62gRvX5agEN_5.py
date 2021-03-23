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

from itertools import compress
def knapsack(capacity, items):
    if capacity>0 and len(items)>0:
        choice=[False]*len(items)
        def knapsack_recursion(item_index,rem_capacity):           
            wt=items[item_index]['weight']
            v=items[item_index]['value']
            if item_index==(len(items)-1):
                if wt<=rem_capacity:
                    choice[item_index]=True
                    return v
                else:
                    choice[item_index]=False
                    return 0
            elif wt<=rem_capacity:
                if v+knapsack_recursion(item_index+1,rem_capacity-wt)>=knapsack_recursion(item_index+1,rem_capacity):
                    choice[item_index]=True
                    return v+knapsack_recursion(item_index+1,rem_capacity-wt)
                else:
                    choice[item_index]=False
                    return knapsack_recursion(item_index+1,rem_capacity)
            else:
                choice[item_index]=False
                return knapsack_recursion(item_index+1,rem_capacity)
        val=knapsack_recursion(0,capacity)
        chosen_items=list(compress(items,choice))
        return {'capacity':capacity,'items':chosen_items,'weight':sum([i['weight'] for i in chosen_items]),'value':val}
    else:
        return {'capacity':0,'items':[],'weight':0,'value':0}

