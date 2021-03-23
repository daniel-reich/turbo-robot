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

def convert_to_roman(num):
  retval = ''
  while num >= 1000:
    retval = retval + 'M'
    num -= 1000
  while num >= 900:
    retval = retval + 'CM'
    num -= 900
  while num >= 500:
    retval = retval + 'D'
    num -= 500
  while num >= 400:
    retval = retval + 'CD'
    num -= 400
  while num >= 100:
    retval = retval + 'C'
    num -= 100
  while num >= 90:
    retval = retval + 'XC'
    num -= 90
  while num >= 50:
    retval = retval + 'L'
    num -= 50
  while num >= 40:
    retval = retval + 'XL'
    num -= 40
  while num >= 10:
    retval = retval + 'X'
    num -= 10
  while num >= 9:
    retval = retval + 'IX'
    num -= 9
  while num >= 5:
    retval = retval + 'V'
    num -= 5
  while num >= 4:
    retval = retval + 'IV'
    num -= 4
  while num >= 1:
    retval = retval + 'I'
    num -= 1
  return retval

