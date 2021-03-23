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
  ans = deg.split('*')
  if '*' in deg :
    if ans[1] == "F" :
      a =  ((((int(ans[0])-32)*5))/9)
      a = round(a)
      return str(a)+ "*C"
    elif ans[1] == "C":
      b = ((int(ans[0]) * (9/5)) + 32)
      b = round(b)
      return str(b) + "*F"
  else:
    return "Error"
​
​
print(convert("35*C"))

