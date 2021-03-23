"""


Atticus has been invited to a dinner party, and he decides to purchase a
bottle of wine. However, he has little knowledge of how to choose a good
bottle. Being a very frugal gentleman (yet disliking looking like a
cheapskate), he decides to use a very simple rule. In any selection of **two
or more wines** , he will always buy the second-cheapest.

Given a list of wine dictionaries, write a function that returns the name of
the wine he will buy for the party. If given an empty list, return `None`. If
given a list of only one, Atticus will buy that wine.

### Examples

    chosen_wine([
      { "name": "Wine A", "price": 8.99 },
      { "name": "Wine 32", "price": 13.99 },
      { "name": "Wine 9", "price": 10.99 }
    ]) ➞ "Wine 9"
    
    chosen_wine([{ "name": "Wine A", "price": 8.99 }]) ➞ "Wine A"
    
    chosen_wine([]) ➞ None

### Notes

All wines will be different prices, so there is no confusion in the ordering.

"""

def chosen_wine(wines):
  if len(wines) ==1:
    return wines[0]["name"]
  if len(wines) == 0:
    return None
  X = wines
  Y = []
  for i in X:
    Y.append(i["price"])
  ind = Y.index(min(Y))
  Y[ind] = max(Y)+1  
  z = Y.index(min(Y))
  return wines[z]["name"]
