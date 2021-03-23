"""


A palindrome is a word, phrase, number or other sequence of characters which
reads the same backward or forward, such as _madam_ or _kayak_.

Write a function that takes a string and determines whether it's a palindrome
or not. The function should return a boolean (`True` or `False` value).

### Examples

    is_palindrome("Neuquen") ➞ True
    
    is_palindrome("Not a palindrome") ➞ False
    
    is_palindrome("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!") ➞ True

### Notes

  * Should be case insensitive.
  * Special characters (punctuation or spaces) should be ignored.

"""

def is_palindrome(txt):
    txt = txt.lower()
    txt = ''.join([x for x in txt if x.isalpha()])
    if txt == txt[::-1]:
        return True
    else:
        return False

