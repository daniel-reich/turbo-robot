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

import re
def complete_pattern(s):
    for c in sorted(set(s) - {'_'}, reverse=True):
        new_s = re.sub('_', c, s)
        pattern = r'(.*[{}].*)(\1)(.*)'.format(c)
        lst = re.findall(pattern, new_s)
        if lst:
            tpl = lst[0]
            if len(tpl) == 3 and new_s == ''.join(tpl):
                len3 = min(len(tpl[0]), len(tpl[2]))
                if tpl[0][:len3] == tpl[2][:len3]:
                    return c
    return -1

