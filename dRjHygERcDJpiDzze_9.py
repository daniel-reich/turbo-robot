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

def lengthen(string,input):
    longest=max([string,input],key=len)
    
    shortest=min([string,input],key=len)
    i,s=divmod(len(longest),len(shortest))
    output=shortest*i+shortest[:s]
    return output

