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
  if '*' not in deg or not deg[-1].isalpha():
    return 'Error'
  
  temp = int(deg[:-2])
  if 'C' in deg:
    temp = 9/5 * temp + 32
    return str(round(temp)) + '*F'
  else:
    temp = 5/9 * (temp - 32)
    return str(round(temp)) + '*C'

