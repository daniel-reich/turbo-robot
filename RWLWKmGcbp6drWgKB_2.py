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
  try:
    lst = list(map(lambda x: wines[x],range(0,len(wines))))
    lst.sort(key = lambda x: x["price"])
    return lst[1]["name"]
  except IndexError:
    if len(wines) == 1:
      return lst[0]["name"]
    else:
      return None

