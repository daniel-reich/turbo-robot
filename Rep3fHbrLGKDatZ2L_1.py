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

def complete_pattern(s):
  for l in range(len(s)//2, 0, -1):
    if all([s[i] == s[i+l] or s[i] == '_' or s[i+l] == '_' for i in range(l)]):
      i = s.find('_')
      return s[:l][i % l] if i >= l else s[l:][i % l]

