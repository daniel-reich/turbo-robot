"""


Write a function that repeats the shorter string until it is equal to the
length of the longer string.

### Examples

    lengthen("abcdefg", "ab") ➞ "abababa"
    
    lengthen("ingenius", "forest") ➞ "forestfo"
    
    lengthen("clap", "skipping") ➞ "clapclap"

### Notes

  * Both strings will differ in length.
  * Both strings will contain at least one character.
  * Either of the two strings could be the shortest in length.

"""

def lengthen(s1, s2):
  n1 = len(s1)
  n2 = len(s2)
  res = ""
  if n1 < n2:
    res = ( (int(n2 / n1) + 1) * s1)[ : n2]
  else:
    res = ( (int(n1 / n2) + 1) * s2)[ : n1]
  return res

