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
    for i in sorted(list(set(s))):
        sc=s
        if i!='_':
            sc=sc.replace('_',i)
            for j in range(1,len(sc)//2+1):
                x=sc[:j]
                r=len(sc)%len(x)
                if (len(sc)//len(x))*x+sc[len(sc)-r:]==sc:
                    return i

