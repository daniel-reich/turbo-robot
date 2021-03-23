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
  if len(s1) > len(s2):
    long = s1
    short = s2
  else:
    long = s2
    short = s1
  new = []
  for i in range(len(long)):
    new.append(short[i%len(short)])
  return ''.join(new)

