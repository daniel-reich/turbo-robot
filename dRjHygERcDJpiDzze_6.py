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
  len_of_longest = max(len(s1), len(s2))
  s1_longer = True
  newstr = ""
  if len_of_longest == len(s2):
    s1_longer = False
  
  if s1_longer:
    for i in range(len(s1) + 1):
      newstr += s2
  else:
    for i in range(len(s2) + 1):
      newstr += s1
  return newstr[:len_of_longest]

