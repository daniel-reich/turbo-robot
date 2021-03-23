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
  q, d, n, p = 0, 0, 0, 0
  while (c - 25) >= 0:
    q += 1
    c = c - 25
  while (c - 10) >= 0:
    d += 1
    c = c - 10
  while (c - 5) >= 0:
    n += 1
    c = c - 5
  p += c
  return dict([('q', q), ('d', d), ('n', n), ('p', p)])

