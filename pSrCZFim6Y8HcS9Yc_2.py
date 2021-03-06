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
  split_deg = deg.split('*')
  
  if len(split_deg) == 1:
    return 'Error'
  else:
    degree = int(split_deg[0])
    unit = split_deg[1]
    converted_unit = 'F'
    if unit == 'C':
      degree = degree * 9 / 5 + 32; 
    else:
      converted_unit = 'C'
      degree = (degree - 32) * 5 / 9
  return str(round(degree)) + '*' + converted_unit

