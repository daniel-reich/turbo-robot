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
  oo = int(o.split('$')[-1])
  nn = int(n.split('$')[-1])
  if oo > nn:
    return ('{}% decrease'.format(round((1 - nn / oo) * 100)))
  else:
    return ('{}% increase'.format(abs(round((1 - nn / oo) * 100))))

