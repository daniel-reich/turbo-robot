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
  digits, alphas = 0, 0 
  digits = sum([digits + 1 for ch in range(len(txt)) if txt[ch].isdigit()])
  alphas = sum([alphas + 1 for ch in range(len(txt)) if txt[ch].isalpha()])
  return {"LETTERS" : alphas, "DIGITS" : digits}

