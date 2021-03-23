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
  convert={'*C': lambda x:round(1.8*x+32), '*F': lambda x:round((x-32)/1.8)}
  try:
    return str(convert[deg[-2:]](int(deg[:-2])))+'*'+chr(137-ord(deg[-1:]))
  except: return "Error"

