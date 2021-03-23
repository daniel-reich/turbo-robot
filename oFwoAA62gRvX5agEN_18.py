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

maxvalue=0
maxtake={}
​
def knapsack(capacity, items):
  global maxvalue
  global maxtake
  maxvalue=0
  maxtake={}
​
  
  def test(take,weight,value):
    global maxvalue
    global maxtake
  # weight=sum([items[t]['weight'] for t in take])
  # value=sum([items[t]['value'] for t in take])
    if weight<=capacity and maxvalue<value:
      maxvalue=value
      maxtake=take
    if weight<=capacity:
      for i in range(max(take+[0]),len(items)):
        if i not in take :
          test(take+ [i], weight+ items[i]['weight'] , value+ items[i]['value']  )
  
  test([],0,0)
​
  print(maxtake)
  itemsout=[items[t] for t in maxtake]
  print(itemsout)
  #itemsout=[]
  out={'capacity':capacity,'items':itemsout,'weight':sum([items[t]['weight'] for t in maxtake]),'value':sum([items[t]['value'] for t in maxtake])}
  return(out)

