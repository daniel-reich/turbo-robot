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

def make_change(c):
  coin_to_penny = {
    'q': 25,
    'd': 10,
    'n': 5,
    'p': 1,
  }
  coins = ['q', 'd', 'n', 'p']
  change = {}
  for coin in coins:
    coin_count = c // coin_to_penny[coin]
    change[coin] = coin_count
    c -= coin_count * coin_to_penny[coin]
  return change

