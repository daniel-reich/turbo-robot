"""


Write a function that swaps the X and Y coordinates in a string.

### Examples

    swap_xy("(1, 2), (3, 4)") ➞ "(2, 1), (4, 3)"
    
    swap_xy("(11, 23), (43, 99)") ➞ "(23, 11), (99, 43)"
    
    swap_xy("(-5, -3), (7, 4)") ➞ "(-3, -5), (4, 7)"

### Notes

  * Some numbers have multiple digits.
  * Some numbers will be negative.

"""

def swap_xy(txt):
​
  indexes = []
  index = []
​
  for n in range(0, len(txt)):
    i = txt[n]
​
    if i == '(':
      index.append(n + 1)
    
    if i == ')':
      index.append(n)
      indexes.append(index)
      index = []
  
  xys = []
​
  for index in indexes:
​
    xindex = int(index[0])
    yindex = int(index[1])
​
    s = ''
​
    for n in range(xindex, yindex):
      s += txt[n]
​
    xys.append(s)
  
  nxys = []
​
  for xy in xys:
    l = list(reversed(xy.split(', ')))
    nxys.append(l)
  
  xys = nxys
  del nxys
​
  template = '({}, {})'
​
  tr = []
​
  for xy in xys:
    x = xy[0]
    y = xy[1]
​
    t = template.format(x, y)
​
    tr.append(t)
  
  return ', '.join(tr)

