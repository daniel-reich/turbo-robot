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
  s1, s2 = min(s1,s2,key=len),max(s1,s2,key=len)
  val1 = len(s2)//len(s1)
  val2 = len(s2)%len(s1)
​
  return s1*val1 + s1[:val2]

