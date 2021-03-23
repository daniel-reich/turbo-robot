"""


You are given a list of strings consisting of grocery items, with prices in
parentheses. Return a list of prices in float format.

### Examples

    get_prices(["salad ($4.99)"]) ➞ [4.99]
    
    get_prices([
      "artichokes ($1.99)",
      "rotiserrie chicken ($5.99)",
      "gum ($0.75)"
    ])
    
    ➞ [1.99, 5.99, 0.75]
    
    get_prices([
      "ice cream ($5.99)",
      "banana ($0.20)",
      "sandwich ($8.50)",
      "soup ($1.99)"
    ])
    
    ➞ [5.99, 0.2, 8.50, 1.99]

### Notes

See if you can use RegExp to solve (but it's not necessary).

"""

def get_prices(lst):
  b = []
  
  for i in lst:
    a = i.split(' ')
    b.append(a)
  
  d = []
  for i in b:
    c = i[len(i)-1][2:len(i[len(i)-1])-1]
    d.append(float(c))
    
  return d

