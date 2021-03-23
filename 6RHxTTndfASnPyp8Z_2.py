"""


The function is given an array of characters. Compress the array into a string
using the following rules. For each group of consecutively repeating
characters:

  * If the number of repeating characters is one, append the string with only this character.
  * If the number `n` of repeating characters `x` is greater than one, append the string with `"x" + str(n)`.

### Examples

    compress(["a", "a", "b", "b", "c", "c", "c"]) ➞ "a2b2c3"
    
    compress(["a"]) ➞ "a"
    
    compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) ➞ "ab12"
    
    compress(["a", "a", "a", "b", "b", "a", "a"]) ➞ "a3b2a2"

### Notes

N/A

"""

from itertools import takewhile
def compress(chars):
  if len(chars) == 1:
    return chars[0]
  if len(set(chars)) == 1:
    return chars[0] + str(len(chars))
  current = chars[0]
  number = len(list(takewhile(lambda x: x == current,chars)))
  chars = chars[number::]
  string = current
  if number > 1:
    string += str(number)
  return string + compress(chars)

