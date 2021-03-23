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

symbols  = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
​
def digitToRN(dig, place):
  if dig < 4:
    return symbols[place] * dig
  elif dig == 4:
    return symbols[place] + symbols[place * 5]
  elif dig < 9:
    return symbols[place * 5] + symbols[place] * (dig - 5)
  else:
    return symbols[place] + symbols[place * 10] 
    
def convert_to_roman(num):
  parts, pv  = [], 1
  while num:
    digit = num % 10
    num = num // 10
    parts.append(digitToRN(digit, pv))
    pv *= 10
  return ''.join(reversed(parts))

