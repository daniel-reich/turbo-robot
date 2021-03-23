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

def is_palindrome(wrd):
  if len(wrd) < 2:
    return True
  if wrd[0] != wrd[-1]:
    return False
  return is_palindrome(wrd[1:-1])

