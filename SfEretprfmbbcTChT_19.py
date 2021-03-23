"""


Given an input string, reverse the string word by word.

### Examples

    reverse_words("the sky is blue") ➞ "blue is sky the"
    
    reverse_words("  hello world!  ") ➞ "world! hello"
    
    reverse_words("a good   example") ➞ "example good a"

### Notes

  * A word is defined as a sequence of non-space characters.
  * The input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
  * Try to solve this in linear time.

"""

def reverse_words(words):
    words = words.lstrip()
    words = words.rstrip()
    split = words.split(" ")
    finalstring = ""
    firstword = split[0]
    index = 1
    reverser = True
    stringmaker = True
    while reverser == True:
        if split[-1] == firstword:
            reverser = False
        else:
            split.insert(0, split[index])
            index += 1
            del split[index]
    while stringmaker == True:
        if not split:
            finalstring = finalstring.lstrip()
            finalstring = finalstring.rstrip()
            stringmaker = False
        else:
            finalstring += split[0] + " "
            del split[0]
    return finalstring

