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
  lil_dicty = {
  "LETTERS": 0,
  "DIGITS": 0
  }
  for i in txt:
    if i.isdigit():
      lil_dicty["DIGITS"] += 1
    elif i.isalpha():
      lil_dicty["LETTERS"] += 1
  return lil_dicty

