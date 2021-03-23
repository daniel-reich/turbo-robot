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
  dct = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
​
  result = ""
  indi_numbers = [int(number) for number in str(num)]
  
  for indi_number, i in zip(indi_numbers, range(len(indi_numbers) - 1, -1, -1)):
    value = indi_number * 10**i
    
    keys = sorted(list(dct.keys()))
    keys.reverse()
    
    while value > 0:
      for key in keys:
        if key <= value:
          value -= key
          result += dct[key]
          break
  
  return result

