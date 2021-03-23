"""


Create a function that converts Celsius to Fahrenheit and vice versa.

### Examples

    convert("35*C") ➞ "95*F"
    
    convert("19*F") ➞ "-7*C"
    
    convert("33") ➞ "Error"

### Notes

  * Round to the nearest integer.
  * If the input is incorrect, return `"Error"`.
  * For the formulae to convert back and forth, check the **Resources** tab.

"""

def convert(deg): 
  try:
    val,unit=deg.split('*')
    val=float(val)
  except ValueError:
    return 'Error'
  if unit=='C':
    return ('%d' % int(round((9*val)/5+32)))+ '*F'
  elif unit=='F':
    return ('%d' % int(round((5*(val-32))/9)))+ '*C'
  else: return 'Error'

