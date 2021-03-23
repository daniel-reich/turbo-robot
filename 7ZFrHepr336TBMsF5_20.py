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

def percentage_changed(o, n):
  p = round(abs(int(o[1:]) - int(n[1:]))*100/int(o[1:]))
  return "{0}% {1}".format(p,"decrease" if int(o[1:])>int(n[1:]) else "increase")

