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

def is_palindrome(w):
  return True if len(w) < 2 else False if \
    w[0] != w[-1] else is_palindrome(w[1:-1])

