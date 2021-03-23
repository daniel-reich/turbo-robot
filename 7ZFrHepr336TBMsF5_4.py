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
  old_price = int(old[1:])
  new_price = int(new[1:])
​
  if old_price > new_price:
    pct_decrease = round((old_price - new_price) / old_price * 100)
    return "{}% decrease".format(pct_decrease)
  elif new_price > old_price:
    pct_increase = round((new_price - old_price) / old_price * 100)
    return "{}% increase".format(pct_increase)

