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
    if len(txt) < 2 or list(txt) == list(reversed(txt)): return 0
    count = 0
    return [len(i) for i in list(reversed([''.join(list(reversed(txt)))[i:] for i in range(len(txt))])) if list(txt+i) == list(reversed(txt+i))][0]

