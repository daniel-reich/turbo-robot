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

def convert(d):
  temp = '';
  if d.find('C') != -1:
    temp = "{}*F".format(round(1.8000 * int(d[0:d.index('C')-1]) + 32));
  elif d.find('F') != -1:
    temp = "{}*C".format(round((int(d[0:d.index('F')-1]) - 32)/1.8));
  else:
    temp = 'Error'
  return temp;

