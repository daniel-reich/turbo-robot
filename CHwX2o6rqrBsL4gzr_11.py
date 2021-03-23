"""


Check if a string `txt` is a title text or not. A title text is one which has
all the words in the text start with an upper case letter.

### Examples

    check_title("A Mind Boggling Achievement") ➞ True
    
    check_title("A Simple Python Program!") ➞ True
    
    check_title("Water is transparent") ➞ False

### Notes

N/A

"""

def check_title(txt):
  return all(ord(word[0]) <= 90 for word in txt.split())
