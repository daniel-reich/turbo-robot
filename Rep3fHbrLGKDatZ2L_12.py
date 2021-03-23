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
  print(s)
  for i in range(1,len(s)):
      missing=set()
      for a,b in zip(s[:i]*(len(s)//i+1),s):
        if a!=b:
          if b=="_":
            missing.add(a)
          elif a=="_":
            missing.add(b)
          else:
            missing.add('_')
​
      if len(missing)==1: return missing.pop()

