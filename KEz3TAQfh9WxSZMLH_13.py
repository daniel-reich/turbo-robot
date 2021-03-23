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

def count_all(string):
    
    alphacount = 0
    digicount = 0
    
    for char in string:
        if char.isdigit():
            digicount += 1
        elif char != " ":
            alphacount += 1            
    
    return {"LETTERS": alphacount, "DIGITS": digicount}

