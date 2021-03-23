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
  if "C" in deg:
    c = int(deg.split("*")[0])
    c = round((c * 9)/5 + 32)
    return str(int(c)) + "*F"
  elif "F" in deg:
    f = int(deg.split("*")[0])
    f = round((5/9) * (f - 32))
    return str(int(f)) + "*C"
  return "Error"

