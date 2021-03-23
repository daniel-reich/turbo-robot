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

def is_palindrome(p,normal = False):
    if not normal:
        p = ''.join(i.lower() for i in p if i.isalpha())
    if len(p) == 1 or len(p) == 0:
        return True
    if p[0] != p[-1]:
        return False
    if p[0] == p[-1]:
        return is_palindrome(p[1:-1],True)

