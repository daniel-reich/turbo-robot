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
  new_old = int(old[1:])
  new_new = int(new[1:])
  result = ""
  percent = round((new_new / new_old) * 100)
  if new_old > new_new:
    result = str(abs(100-percent))+"%"+" "+"decrease"
  elif new_old < new_new:
    result = str(abs(100-percent))+"%"+" "+"increase"
  return result

