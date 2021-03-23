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
  old, new = int(old[1:]), int(new[1:])
  if old > new:
    return str(abs(round((1 - new / old) * 100))) + '% decrease'
  return str(abs(round((1 - new / old) * 100))) + '% increase'

