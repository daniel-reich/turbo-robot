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

def complete_pattern(s, lst = ""):
    for i in s: lst += i if i not in (lst+"_") else ""
    pos, change, long  = s.find("_"), list(s), len(s)
    for i in lst:
        change[pos] = i; cp = "".join(change)
        for let in range(1, long//2+1):
            for nex in range(let, long+1, let ):
                if cp[nex:nex+let] not in cp[:let]: break
                if nex+let>long: return i

