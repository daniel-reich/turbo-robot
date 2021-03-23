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

def is_palindrome(wrd, n=1):
  if wrd[n - 1] != wrd[-n]:
    return False
  return is_palindrome(wrd, n + 1) if n < len(wrd) else True

