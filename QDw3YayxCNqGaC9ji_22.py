"""


Create a function that takes an amount of monetary change (e.g. 47 cents) and
breaks down the most efficient way that change can be made using USD quarters,
dimes, nickels and pennies. Your function should return a dictionary.

### Examples

    make_change(47) ➞ { "q": 1, "d": 2, "n": 0, "p": 2 }
    
    make_change(24) ➞ { "q": 0, "d": 2, "n": 0, "p": 4 }
    
    make_change(92) ➞ { "q": 3, "d": 1, "n": 1, "p": 2 }

### Notes

Amount given will always be less than 100 and more than 0.

"""

import math as m
​
def make_change(c):
  cnt = [0, 0, 0, 0]
  coins = [25, 10, 5, 1]  
  for x in range(0,4):
    cnt[x] = m.floor(c/coins[x])
    c -= cnt[x]*coins[x]
  return {'q': cnt[0], 'd': cnt[1], 'n': cnt[2], 'p': cnt[3]}

