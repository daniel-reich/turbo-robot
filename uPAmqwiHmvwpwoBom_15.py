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
  result = ''
  while num > 0:
    if num >= 1000:
      result += 'M'
      num -= 1000
    elif num >= 900:
      result += 'CM'
      num -= 900
    elif num >= 500:
      result += 'D'
      num -= 500
    elif num >= 400:
      result += 'CD'
      num -= 400
    elif num >= 100:
      result += 'C'
      num -= 100
    elif num >= 90:
      result += 'XC'
      num -= 90
    elif num >= 50:
      result += 'L'
      num -= 50
    elif num >= 40:
      result += 'XL'
      num -= 40
    elif num >= 10:
      result += 'X'
      num -= 10
    elif num == 9:
      result += 'IX'
      num = 0
    elif num >= 5:
      result += 'V'
      num -= 5
    elif num == 4:
      result += 'IV'
      num = 0
    elif num >= 1:
      result += 'I'
      num -= 1
  return result

