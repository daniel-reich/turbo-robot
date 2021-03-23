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
  import pandas as pd
  i=0
  df=pd.DataFrame(columns=['name','weight','value'])
  for item in items:
    df.loc[i,'name']=item['name']
    df.loc[i,'weight']=item['weight']
    df.loc[i,'value']=item['value']
    i+=1
  if(len(items)>4):
    df=df.sort(['value'],ascending=False).reset_index()
  else:
    df=df.sort(['weight']).reset_index()
  items_, items1,weight, value =[],[],0,0
  for i in range (df.shape[0]):
    if (weight+df.loc[i,'weight']<=capacity):
      items_.append({'name':df.loc[i,'name'],'weight':df.loc[i,'weight'],'value':df.loc[i,'value']})
      weight +=df.loc[i,'weight']
      value +=df.loc[i,'value']
  for item in items:
    if (item in items_):
      items1.append(item)
  return {'capacity': capacity, 'items': items1, 'weight': weight, 'value': value}

