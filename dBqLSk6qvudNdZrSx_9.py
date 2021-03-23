"""


Create a function that determines if the `temp` of the water is considered
boiling or not. `temp` will be measured in fahrenheit and celsius.

### Examples

    is_boiling("212F") ➞ True
    
    is_boiling("100C") ➞ True
    
    is_boiling("0F") ➞ False

### Notes

The boiling point of water is 212F in fahrenheit and 100C in celsius.

"""

def is_boiling(temp):
​
  t = temp[0:len(temp)-1]
  type = temp[len(temp)-1:]
  if type == "F":
    if int(t) >= 212:
      return True
    else:
      return False
  elif type == "C":
    if int(t) >= 100:
      return True
    else:
      return False

