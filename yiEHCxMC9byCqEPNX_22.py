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

def is_palindrome(p):
  if len(p) <2:
    return True
  elif not p.isalpha():
    newP = ''
    for _,char in enumerate(p):
      if char.isalpha():
        newP += char
    return is_palindrome(newP.lower())
  else:
    first = p[0];last = p[-1]
    return first.lower() == last.lower() and is_palindrome(p[1:-1])

