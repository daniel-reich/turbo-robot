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
  l1=len(s1)
  l2=len(s2)
  if(l1>l2):
    a=s2*10
    r=l1-l2
    return s2+a[:r]
  else:
    a=s1*10
    r=l2-l1
    return s1+a[:r]

