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

import re
​
def count_all(txt):
  liczba_digits=len(re.findall(r"\d",txt))
  liczba_char=len(re.findall(r"[a-zA-Z]",txt))
  wynik=dict([("LETTERS",liczba_char),("DIGITS",liczba_digits)])
  return wynik

