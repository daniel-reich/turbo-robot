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

roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
arabic = [1000, 900, 500, 400, 100, 90, 50,40, 10, 9, 5, 4, 1]
def convert_to_roman(num):
  roman_number = ""
  while num > 0:
    x = 0
    while True:
      if num - arabic[x] >= 0:
        num = num- arabic[x]
        roman_number += roman[x]
        break
      x += 1
  return roman_number

