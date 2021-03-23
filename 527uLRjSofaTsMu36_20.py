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
  if word != '':
    if len(word) % 2 == 0:  
      return word[len(word) // 2 - 1] + word[len(word) // 2]
    return word[len(word) // 2]
  return ''

