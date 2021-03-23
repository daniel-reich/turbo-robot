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
  return "{0}*F".format(round(int(deg[:-2]) * 9/5 + 32)) if (deg.split("*")[-1] == "C") else "{0}*C".format(round((int(deg[:-2]) - 32)*5/9)) if (deg.split("*")[-1] =="F") else "Error"

