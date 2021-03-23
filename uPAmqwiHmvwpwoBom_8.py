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
  roman = ""
​
  roman += "M" * int(num / 1000)
  num %= 1000
  roman += "CM" * int(num / 900)
  num %= 900
  roman += "D" * int(num / 500)
  num %= 500
  roman += "CD" * int(num / 400)
  num %= 400
  roman += "C" * int(num / 100)
  num %= 100
  roman += "XC" * int(num / 90)
  num %= 90
  roman += "L" * int(num / 50)
  num %= 50
  roman += "XL" * int(num / 40)
  num %= 40
  roman += "X" * int(num / 10)
  num %= 10
  roman += "IX" * int(num / 9)
  num %= 9
  roman += "V" * int(num / 5)
  num %= 5
  roman += "IV" * int(num / 4)
  num %= 4
  roman += "I" * int(num)
  
  return roman

