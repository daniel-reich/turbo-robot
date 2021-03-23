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
  if int(old[1:]) > int(new[1:]):
    return '{}% decrease'.format(int(((int(old[1:]) - int(new[1:])) / int(old[1:]))*100))
  else:
    return '{}% increase'.format(abs(int(((int(old[1:]) - int(new[1:])) / int(old[1:]))*100)))

