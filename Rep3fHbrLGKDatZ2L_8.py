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
  n = len(s)
  for i in range(1,n):
    pieces = {s[a:a+i] for a in range(0, n - n%i, i)}
    om_lst = [p for p in pieces if '_' in p]
    oth_lst = [p for p in pieces if '_' not in p]
    if len(oth_lst) == 1:
      oth = oth_lst[0]
      if len(om_lst)==1:
        om = om_lst[0]
        idx = om.index('_')
        if om[:idx] == oth[:idx] and om[idx+1:] == oth[idx+1:]:
          return oth[idx]
      elif len(om_lst)==0:
        idx = s[n-n%i:].index('_')
        return s[idx]

