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
​
  ones = {'0': '', '1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX', None: ''}
  tens = {'0': '', '1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC', None: ''}
  hundreds = {'0': '', '1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM', None: ''}
  thousands = {'0': '', '1': 'M', '2': 'MM', '3': 'MMM', None: ''}
​
  tv = None
  hv = None
  t2v = None
  ov = None
​
  num = str(num)
​
  if len(num) == 4:
    tv = num[0]
    hv = num[1]
    t2v = num[2]
    ov = num[3]
  elif len(num) == 3:
    hv = num[0]
    t2v = num[1]
    ov = num[2]
  elif len(num) == 2:
    t2v = num[0]
    ov = num[1]
  elif len(num) == 1:
    ov = num[0]
  else:
    return 'Incorrect Number: {}'.format(num)
  
  roman = [thousands[tv], hundreds[hv], tens[t2v], ones[ov]]
​
  return ''.join(roman)

