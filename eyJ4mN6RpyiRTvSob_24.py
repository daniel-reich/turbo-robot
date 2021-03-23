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
  l = list(txt)
  true = 0
  for a in l:
    if l.count(a) % 2 == 0:
      true = true + 1
  return True if (true == len(l) - 1 and len(l) % 2 == 1) or (true == len(l) and len(l) % 2 == 0) else False

