"""


Given an _incomplete palindrome_ as a string, return the **minimum letters
needed** to be added on to the **end** to make the string a **palindrome**.

### Examples

    min_palindrome_steps("race") ➞ 3
    # Add 3 letters: "car" to make "racecar"
    
    min_palindrome_steps("mada") ➞ 1
    # Add 1 letter: "m" to make "madam"
    
    min_palindrome_steps("mirror") ➞ 3
    # Add 3 letters: "rim" to make "mirrorrim"

### Notes

Trivially, words which are already palindromes should return `0`.

"""

def min_palindrome_steps(txt):
  return len(txt) - max((len(txt[i:]) for i in range(0, len(txt)) if is_palindrome(txt[i:])) or [1])
  
  
def is_palindrome(w):
  return w == w[::-1]

