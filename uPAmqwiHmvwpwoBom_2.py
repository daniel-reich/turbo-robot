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
  decimal = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
  numeral = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
  res = ''
  for i in range(13):
    val = num//decimal[i]
    if val:
      res += numeral[i] * val
      num -= decimal[i] * val
  return res

