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

def compress(lst):
  res = []
  mini = []
  l = len(lst)
  for i in range(l):
    if i != 0 and lst[i] != lst[i-1]:
      res.append(mini)
      mini = []
      mini.append(lst[i])
      if i == l - 1:
        res.append(mini)
    else:
      mini.append(lst[i])
      if i == l - 1:
        res.append(mini)
  result = [''.join(i) for i in res]
  return ''.join([i if len(i) == 1 else "{}{}".format(i[0], len(i)) for i in result])

