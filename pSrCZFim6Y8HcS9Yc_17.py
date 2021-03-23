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
    d, t = deg.split('*')
  except ValueError:
    return 'Error'
  if t == 'C': 
    return '{:.0f}*F'.format(int(d) * 1.8 + 32)
  elif t =='F':
    return '{:.0f}*C'.format((int(d) -32) / 1.8 )

