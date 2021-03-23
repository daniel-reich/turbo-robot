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

def convert(n):
  return  '{}*F'.format(round(int(n.split('*')[0])*1.8+32)) if 'C' in n else '{}*C'.format(round((int(n.split('*')[0])-32)/1.8)) if 'F' in n else 'Error'

