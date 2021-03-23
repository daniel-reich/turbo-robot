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

import re
def is_palindrome(txt):
  a = re.sub(r',|!|-', '', txt)
  b = a.replace(' ', '')
  return b.lower() == b[::-1].lower()
