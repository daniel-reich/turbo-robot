"""


Create a function that takes a string and returns the middle character(s). If
the word's length is odd, return the middle character. If the word's length is
even, return the middle two characters.

### Examples

    get_middle("test") ➞ "es"
    
    get_middle("testing") ➞ "t"
    
    get_middle("middle") ➞ "dd"
    
    get_middle("A") ➞ "A"

### Notes

All test cases contain a single word (as a string).

"""

def get_middle(word):
  mid = (len(word)//2)-1
  
  if len(word) % 2:
    return word[mid+1]
  else:
    return word[mid:mid+2]
