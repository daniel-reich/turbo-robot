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
    txt_list = list(txt)
    temp = txt_list.copy()
    if txt == txt[::-1]:
        return 0
    for i in range(1, len(txt_list)+1):
        reverse = reversed(txt_list[0:i])
        temp.extend(reverse)
        if temp == temp[::-1]:
            return i
        else:
            temp = txt_list.copy()
            continue

