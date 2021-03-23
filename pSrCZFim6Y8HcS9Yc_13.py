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
    C = lambda c: str(int(round(int(c) * 1.8 + 32))) + '*F'
    F = lambda f: str(int(round((int(f) - 32) / 1.8))) + '*C'
    return eval(deg[-1])(deg.split('*')[0]) if '*' in deg else 'Error'

