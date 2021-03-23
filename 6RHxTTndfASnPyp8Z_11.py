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

def compress(chars):
  chars = "".join(chars) + " "
  result = ""
  count = 0
  for i, l in enumerate(chars):
    if i == 0:
      count += 1
    else:
      if l != chars[i-1]:
        if count == 1:
          result += chars[i-1]
        else:
          result += chars[i-1] + str(count)
        count = 1
      else:
        count += 1
  return result

