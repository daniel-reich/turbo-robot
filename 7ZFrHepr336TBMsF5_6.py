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
  percentage = abs(100 - round((int(str(new)[1:]) * 100) / int(str(old)[1:])))
  if int(new[1:]) < int(old[1:]):
    return str(percentage) + '% decrease'
  
  return str(percentage) + '% increase'

