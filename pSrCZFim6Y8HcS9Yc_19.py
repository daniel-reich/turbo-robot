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
  split_deg = deg.split("*")
​
  if len(split_deg) == 1:
    return "Error"
​
  elif split_deg[-1] == "C":
    return str(round(int(split_deg[0]) * 1.8 + 32)) + "*F"
​
  elif split_deg[-1] == "F":
    return str(round((int(split_deg[0]) - 32) * 5/9)) + "*C"

