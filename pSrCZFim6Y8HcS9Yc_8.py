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
    if deg[-2::] == '*C':
        return celsius_farenheit(int(deg[:-2]))
    elif deg[-2::] == '*F':
        return farenheit_celsius(int(deg[:-2]))
    return 'Error'
  
def celsius_farenheit(n):
    return str(round((n * 9/5) + 32)) + '*F'
​
def farenheit_celsius(n):
    return str(round((n - 32) * 5/9)) + '*C'

