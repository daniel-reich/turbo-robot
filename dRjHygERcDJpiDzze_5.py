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
  a=s1
  b=s2
  if len(a)>len(b):
    x=a
    y=b
  else:
    x=b
    y=a
  for i in x:
    for j in y:
      if len(x)!=len(y):
        y+=j
  return(y)

