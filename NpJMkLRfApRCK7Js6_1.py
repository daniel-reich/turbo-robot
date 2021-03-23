"""


Create a **recursive** function that determines whether a word is a
**palindrome** or not.

### Examples

    is_palindrome("madam") ➞ true
    
    is_palindrome("adieu") ➞ false
    
    is_palindrome("rotor") ➞ true

### Notes

  * All inputs are in lowercase.
  * You are expected to solve this challenge via **recursion**.
  * You can check on the **Resources** tab for more details about _recursion_.

"""

def is_palindrome(word):
  if len(word) <= 1:
    return True
  elif word[0] != word[-1]:
    return False
  return is_palindrome(word[1:-1])

