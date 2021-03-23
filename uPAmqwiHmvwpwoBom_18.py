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
    output = ''
    table = {
        1000: 'M',
         900: 'CM',
         500: 'D',
         400: 'CD',
         100: 'C',
          90: 'XC',
          50: 'L',
          40: 'XL',
          10: 'X',
          9: 'IX',
          5: 'V',
          4: 'IV',
          1: 'I',
    }
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    for n in numbers:
        while num >= n:
            num -= n
            output += table[n]
    
    return output

