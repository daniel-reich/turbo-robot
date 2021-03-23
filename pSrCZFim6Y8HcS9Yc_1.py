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
  x = deg.replace('C', '').replace('F', '').replace('*', '')
  if 'C' in deg:
    t = round(int(x) * 9 / 5 + 32)
    return str(t) + '*F'
  elif 'F' in deg:
    t = round(5 / 9 * (int(x) - 32))
    return str(t) + '*C'
  else:
    return 'Error'

