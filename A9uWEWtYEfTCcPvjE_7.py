"""


Create a function that returns a list of the most important items purchasable
with a given budget. You will be given a dictionary `dct` containing items and
their respective price and importance, and you will also be given a budget `b`
to restrict the number of items you can buy. The importance can only be from
1-10, whereas the price and budget can be anything.

### Example

    price_importance_sort({
      "apples": { "price": 5, "importance": 3 },
      "oranges": { "price": 3, "importance": 2},
      "pears": { "price": 2,  "importance": 2}
    }, 5) ➞ ["oranges", "pears"]

The oranges and pears can be purchased at budget with a total importance of
`4`. Apples and oranges or pears are not able to be purchased due to the
budget and apples themselves only have an importance value of `3`, making the
oranges/pears group preferable.

### Notes

  * More importance is better, not worse (it isn't a 1st/2nd/3rd ranking).
  * The whole budget may be used.
  * In the case of a tie, use the cheaper/more important of the two.
  * Order the final list alphabetically.

"""

def price_importance_sort(dct, b):
​
  class Item:
​
    def __init__(self, name, price, importance):
      self.name = name
      self.price = price
      self.imp = importance
    
  class Budget:
​
    def __init__(self, budget):
      self.budget = budget
    
    def best_purchase(self, items):
      from itertools import permutations as c
     # print(len(items), items)
      combinations = []
​
      for n in range(1, len(items) + 1):
      #  print(n)
        p = list(c(range(len(items)), n))
       # print(p)
        for item in p:
          combinations.append(item)
      
      valid_purchases = []
​
      for comb in combinations:
        if [items[c] for c in comb] not in valid_purchases and list(reversed([items[c] for c in comb])) not in valid_purchases:
          purchase = [items[c] for c in comb]
​
      
          total_price = 0
          for item in purchase:
            total_price += item.price
          if total_price <= self.budget:
            valid_purchases.append(purchase)
      
      important_values = {}
      budget_costs = {}
​
      for purchase in valid_purchases:
        importance = 0
        for i in purchase:
          #print(i)
          importance += i.imp
        if importance not in important_values.keys():
          important_values[importance] = [purchase]
        else:
          important_values[importance].append(purchase)
        price = sum([i.price for i in purchase])
        budget_costs[str(purchase)] = price
      
      if len(important_values[max(list(important_values.keys()))]) == 1:
        return [i.name for i in important_values[max(list(important_values.keys()))][0]]
      else:
        minim = self.budget
        to_go = None
​
        for item in important_values[max(list(important_values.keys()))]:
          if budget_costs[str(item)] < minim:
            to_go = item
            minim = budget_costs[str(item)]
        
        tr = [i.name for i in to_go]
​
        return sorted(tr)
  
  items = []
​
  for item in dct.keys():
    items.append(Item(item, dct[item]['price'], dct[item]['importance']))
  
  budget = Budget(b)
​
  return budget.best_purchase(items)

