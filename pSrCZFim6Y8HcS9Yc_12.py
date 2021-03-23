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
    t,c = deg.split('*')
    return str(round(int(t) * 9/5 + 32)) + '*F' if c=='C' else str(round((int(t) - 32) * 5/9)) + '*C'
  except:
    return "Error"

