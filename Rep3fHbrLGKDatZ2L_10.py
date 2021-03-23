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
    index = s.find("_")
    for item in set(s) - {'_'}:
        complete_string = s.replace("_", item)
        for k in range(1, len(s)//2+1):
            if all(complete_string[i:i+k] == complete_string[0:k] for i in range(0, len(s), k) if i + k <= len(s)):
                if k-1 >= index:
                    return item
                else:
                    return s[index % k]

