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
    num = int(deg[:-2])
    if deg[-1] == 'C':
      return "{}*F".format(round(num * 9/5) + 32, 0)
    return "{}*C".format(round((num - 32) * 5/9), 0)
  except:
    return 'Error'

