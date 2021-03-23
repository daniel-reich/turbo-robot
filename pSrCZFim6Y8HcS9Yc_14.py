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
    if '*' not in deg:return 'Error'
    val = int(deg.split('*')[0])
    inFahrenheit = round(val * 1.8 + 32)
    inCelsius = round((val - 32) / 1.8)
    return str(inCelsius)+'*C' if 'F' in deg else str(inFahrenheit) + '*F'

