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
  a = 0
  b = 0
  for x in range(0, len(txt)):
    if txt[x].isdigit() == True:
      a += 1 
    if txt[x].isalpha() == True:
      b += 1
  mydict = {"LETTERS" : b, "DIGITS" : a}
  return mydict

