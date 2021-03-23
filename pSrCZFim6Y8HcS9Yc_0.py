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
​
    try:
      temp, unit = deg.split('*')
    except:
      return 'Error'
    
    if unit == 'F':
      return str(round((int(temp) - 32) / 1.8)) + '*' + 'C'
      
    if unit == 'C':
      return str(round((int(temp) * 1.8) + 32)) + '*' + 'F'

