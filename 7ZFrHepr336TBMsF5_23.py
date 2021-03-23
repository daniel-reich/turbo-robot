"""


Create a function that takes an old price `old`, a new price `new`, and
returns what percent the price decreased or increased. Round the percentage to
the nearest whole percent.

### Examples

    percentage_changed("$800", "$600") ➞ "25% decrease"
    
    percentage_changed("$1000", "$840") ➞ "16% decrease"
    
    percentage_changed("$100", "$950") ➞ "850% increase"

### Notes

N/A

"""

def percentage_changed(old, new):
  woohoo = 0
​
  old1 = int(old[1:])
  neww = int(new[1:])
  woohoo = round(abs((neww - old1) / old1 * 100))
  if old1 >= neww:
    return str(woohoo) + '%' + ' ' + 'decrease'
  else:
    return str(woohoo) + '%' + ' '+ 'increase'
print(percentage_changed("$100", "$950"))

