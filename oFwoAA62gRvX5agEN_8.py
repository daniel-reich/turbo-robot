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
    result = []
    def helper(capacity,items,lst=[],weight=0,val=0):
        if weight <= capacity:
            result.append([lst,val])
        for i in range(len(items)):
            helper(capacity,items[i+1:],lst+[items[i]],weight+items[i]['weight'],val+items[i]['value'])
​
    helper(capacity,items)
    result = max(result,key=lambda x:x[1])
    return{'capacity':capacity,'items':result[0],'weight':sum(i['weight'] for i in result[0]),'value':result[1]}

