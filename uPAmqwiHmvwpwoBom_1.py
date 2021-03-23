"""


Create a function that takes an Arabic number and converts it into a Roman
number.

### Examples

    convert_to_roman(2) ➞ "II"
    
    convert_to_roman(12) ➞ "XII"
    
    convert_to_roman(16) ➞ "XVI"

### Notes

  * All roman numerals should be returned as uppercase.
  * The largest number that can be represented in this notation is 3,999.

"""

breakpoints = [(1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'),
               (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'),
               (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]
    
def convert_to_roman(num):
    for val, token in reversed(breakpoints):
        if num >= val:
            return token + convert_to_roman(num-val)
    return ''

