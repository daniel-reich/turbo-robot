"""


You will be given a string that is made up of some repeated pattern of
characters. However, one of the characters in the string will be missing and
replaced by an underscore. Write a function that returns the missing
character.

### Examples

    complete_pattern("ABCABCA_CAB") ➞ "B"
    
    complete_pattern("_ABAABAABA") ➞ "A"
    
    complete_pattern("X+X*X+X*X+X_") ➞ "*"

### Notes

  * The pattern will be repeated in full at least twice, though one of those repetitions may contain the missing character.
  * The string may end in the middle of a repetition of the pattern.
  * The pattern will never contain an underscore.

"""

from itertools import cycle
def complete_pattern(s):
  S=set(s.replace('_', ''))
  res=''
  for x in S:
    p=s.replace('_', x)
    if any(all(x==y for x, y in zip(p,cycle(p[:i]))) for i in range(1, len(p)//2+1)):
      res+=x
  return res

