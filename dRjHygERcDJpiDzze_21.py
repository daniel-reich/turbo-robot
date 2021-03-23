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
        long, short = s1, s2
    else:
        long, short = s2, s1
    integer = len(long)//len(short)
    residual = len(long)%len(short)
    return integer*short + short[:residual]

