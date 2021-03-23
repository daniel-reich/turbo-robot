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
  def splitter(chars):
    nl = []
    l = []
    
    for char in chars:
      if l == []:
        l.append(char)
      elif l[0] == char:
        l.append(char)
      else:
        nl.append(l)
        l = [char]
    
    if l != []:
      nl.append(l)
    
    return nl
  string = lambda lst: lst[0] if len(lst) == 1 else lst[0] + str(len(lst))
  
  s = splitter(chars)
  
  return ''.join([string(s[n]) for n in range(len(s))])

