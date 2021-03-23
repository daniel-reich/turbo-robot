"""


A palindrome is a series of letters or numbers that reads equivocally
backwards. Write a **recursive** function that determines whether a given
string is a **palindrome** or not.

### Examples

    is_palindrome("Go hang a salami, I'm a lasagna hog!") ➞ True
    
    is_palindrome("This phrase, surely, is not a palindrome!") ➞ False
    
    is_palindrome("Eva, can I see bees in a cave?") ➞ True

### Notes

  * Symbols and special characters should be ignored.
  * You are expected to solve this challenge via **recursion**.
  * You can check on the **Resources** tab for more details about _recursion_.

"""

def is_palindrome(p, r = None, i = None):
  if r == None:
    symbols = list('/?,.><@#-_!$%^~\';:')
    for symbol in symbols:
      p = p.replace(symbol, '')
    p = p.lower().replace(' ', '')
    r = ''.join(list(reversed(p)))
    i = 0
    return is_palindrome(p, r, i)
  elif i == len(p) - 1:
    return p[i] == r[i]
  else:
    if p[i] == r[i]:
      i += 1
      return is_palindrome(p, r, i)
    else:
      return False

