"""


Mubashir needs to assemble a parcel of **ordered** chocolates. He got two
types of chocolates:

  *  **Small chocolates (2 grams each)**
  *  **Big chocolates (5 grams each)**

Create a function that takes three parameters: Number of small available
chocolates `n_small`, number of big chocolates available `n_big` and desired
weight (in grams) of the final parcel `order`.

The function should return the **required number of small chocolates** to
achieve the goal. The function should return `-1` if the goal cannot be
achieved by any possible combinations of small and big chocolates.

### Examples

    chocolates_parcel(4, 1, 13) ➞ 4
    # 4 small chocolates = 8 grams
    # 1 big chocolate = 5 grams
    # 8 + 5 = 13 grams
    # Required number of small chocolates = 4
    
    chocolates_parcel(4, 1, 14) ➞ -1
    # You can not make any combination to reach 14 grams.
    
    chocolates_parcel(2, 1, 7) ➞ 1
    # 1 big chocolate = 5 grams
    # 1 small chocolates = 2 grams
    # 5 + 2 = 7 grams
    # Required number of small chocolates = 1

### Notes

  * Maximize the use of big chocolates that are available to achieve the desired goal. And only then should you proceed to use the small chocolates.
  * You can't break chocolates into small pieces.

"""

import itertools
def chocolates_parcel(n_small, n_big, order):
  res = []
  for c in itertools.product(list(range(n_small+1)), list(range(n_big+1))):
    if c[0]*2 + c[1]*5 == order:
      res.append((c[0], c[1]))
  if res == []:
    return -1 
  else:
    return sorted(res)[0][0]

