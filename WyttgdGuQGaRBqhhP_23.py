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

def is_palindrome(st):
    return st == st[::-1]
​
​
​
​
def min_palindrome_steps(n_word):
    x = 0
    addition = ""
    while not is_palindrome(n_word + addition):
        addition = n_word[x] + addition
        print(n_word+addition)
        x += 1
    return x

