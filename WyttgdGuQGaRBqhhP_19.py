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

def min_palindrome_steps(s):
    st = 0
    i, j = 0, len(s)-1
    while i <= j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            j = len(s) -1
            st += 1
            i = st
    return st

