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
  t = int(temp[:-1])
  return t>=212 if 'F' in temp else t>=100

