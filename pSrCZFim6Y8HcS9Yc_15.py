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
  if deg[-1] not in 'FC': return 'Error'
  f = str(round(int(deg[:-2])*1.8+32))+ '*F'
  c = str(round((int(deg[:-2])-32)/1.8))+ '*C'
  return f if deg[-1]=='C' else c

