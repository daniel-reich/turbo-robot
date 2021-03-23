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
  per = (int(new[1:])/int(old[1:])*100)-100
  change = 'decrease' if per<0 else 'increase'
  return '{}% {}'.format(round(abs(per)),change)

