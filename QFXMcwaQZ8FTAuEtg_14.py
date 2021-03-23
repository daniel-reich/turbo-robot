"""


Create a function that takes a single character as an argument and returns the
char code of its lowercased / uppercased counterpart.

### Examples

    Given that:
      - "A" char code is: 65
      - "a" char code is: 97
    
    counterpartCharCode("A") ➞ 97
    
    counterpartCharCode("a") ➞ 65

### Notes

  * The argument will always be a single character.
  * Not all inputs will have a counterpart (e.g. numbers), in which case return the inputs char code.

"""

def counterpartCharCode(char):
  if ord(char) >= 65 and ord(char) <= 90:
    return ord(char) + 32
  elif ord(char) >= 97 and ord(char) <= 122:
    return ord(char) - 32
  else: 
    return ord(char)

