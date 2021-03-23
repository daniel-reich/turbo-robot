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
    dct = {'F': 212, 'C': 100}
    return int(temp[:-1]) >= dct[temp[-1]]

