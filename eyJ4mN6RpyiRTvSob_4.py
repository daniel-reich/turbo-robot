"""


Given a word, create a function which returns whether or not it's possible to
**create a palindrome** by _rearranging the letters in the word_.

### Examples

    is_palindrome_possible("rearcac") ➞ True
    # You can make "racecar"
    
    is_palindrome_possible("suhbeusheff") ➞ True
    # You can make "sfuehbheufs" (not a real word but still a palindrome)
    
    is_palindrome_possible("palindrome") ➞ False
    # It's impossible

### Notes

  * Trivially, words which are already palindromes return `True`.
  * Words are given in all _lowercase_.

"""

def is_palindrome_possible(txt):
  oddcount=0
  for char in txt:
    if txt.count(char)%2 != 0:
      oddcount+=1/txt.count(char)
  if oddcount>1:
    return False
  else:
    return True

