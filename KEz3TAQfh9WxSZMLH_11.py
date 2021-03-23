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

def is_letter(char):
  return ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z')
​
def is_number(char):
  return ord('0') <= ord(char) <= ord('9')
​
def count_all(txt):
  dictionary = {}
  dictionary["LETTERS"] = 0
  dictionary["DIGITS"] = 0
  for char in txt:
    dictionary["LETTERS"] += is_letter(char)
    dictionary["DIGITS"] += is_number(char)
  return dictionary

