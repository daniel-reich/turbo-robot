"""


Write a function that takes a string and calculates the number of letters and
digits within it. Return the result in a dictionary.

### Examples

    count_all("Hello World") ➞ { "LETTERS":  10, "DIGITS": 0 }
    
    count_all("H3ll0 Wor1d") ➞ { "LETTERS":  7, "DIGITS": 3 }
    
    count_all("149990") ➞ { "LETTERS": 0, "DIGITS": 6 }

### Notes

  * Tests contain only alphanumeric characters.
  * Spaces are not letters.
  * All tests contain valid strings.

"""

def count_all(txt):
  num = "0123456789"
  str = "abcdefghijklmnopqrstuvwxyz"
  dict = {'LETTERS': 0, 'DIGITS': 0}
  #numCount = 0
  #strCount = 0
  for item in txt:
    if item in num:
      dict['DIGITS'] += 1
      #numCount += 1
    if item.lower() in str:
      dict['LETTERS'] += 1    
      #strCount += 1
  return dict

