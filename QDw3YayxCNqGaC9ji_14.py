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
  change_dict = {}
  remainder = c%25
  change_dict['q'] = abs(int((c - remainder)/25))
  remainder1 = remainder%10
  change_dict['d'] = abs(int((remainder1 - remainder)/10))
  remainder2 = remainder1%5
  change_dict['n'] = abs(int((remainder2 - remainder1)/5))
  remainder3 = remainder2%1
  change_dict['p'] = abs(int(remainder3 - remainder2))
  return change_dict

