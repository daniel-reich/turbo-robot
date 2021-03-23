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

def check_pattern(s):
    n = len(s)
    for k in range(2, len(s) // 2 + 1):
        pattern = s[:k]
        long = pattern * (2 + n // k)
        if long[:n] == s and n >= 2 * k:
            return True
    return False
​
def complete_pattern(s):
    unique = set(s.replace('_', ''))
    if len(s) == 2:
        return list(unique)[0]
    for c in unique:
        s2 = s.replace('_', c)
        if check_pattern(s2):
            return c

