"""


You arrive at the supermarket checkout and you've only got a limited number of
shopping bags with you. Miser that you are, you hate buying extra bags when
you've got dozens at home that you forgot to bring with you!! Can you fit all
your shopping into the bags you've got with you?

Each bag can carry a maximum of 10kg and each item you've purchased weighs
between 1 and 10kg.

Create a function that takes two parameters, a list of the weights of each
item and the number of bags you are carrying. Return `True` if there are
enough bags to contain all the items, otherwise `False`.

### Example

    can_fit([2, 1, 2, 5, 4, 3, 6, 1, 1, 9, 3, 2], 4) ➞ True
    # Bag 1 = [2, 1, 2, 5] (10kg)
    # Bag 2 = [4, 3, 3] (10kg)
    # Bag 3 = [6, 2, 1, 1] (10kg)
    # Bag 4 = [9] (9kg)
    
    can_fit([2, 7, 1, 3, 3, 4, 7, 4, 1, 8, 2], 4) ➞ False
    # Bag 1 = [2, 8] (10kg)
    # Bag 2 = [3, 7] (10kg)
    # Bag 3 = [2, 4, 4] (10kg)
    # Bag 4 = [7, 3] (10kg)
    # two 1kg items left over!

### Notes

  * All weights will be integers between 1 and 10kg inclusive
  * Items can be packed in any order
  * There may be more than one way to fit all the items in the available bags

 ** _Based on an easier challenge[ How Many
Boxes?](https://edabit.com/challenge/QdEAMeXNJAivcTMiT) by @zatoichi49._**

"""

def can_fit(weights, bags):
  # method: pack largest first
  cap = 10
  weights = sorted(weights, reverse=True)
  nb = 0
  while weights:
    # pick largest first
    w = weights.pop(0)
    i = 0
    while i < len(weights):
      if weights[i] <= cap - w:
        w += weights.pop(i)
      else:
        i += 1
    nb += 1
  return nb <= bags

