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

def is_palindrome(txt):
    rev_txt_list = list(txt)
    rev_txt_list.reverse()
    rev_txt = "".join(rev_txt_list)
    if (rev_txt == txt):
        return 1
    else:
        return 0
​
​
def min_palindrome_steps(txt):
    if (is_palindrome(txt)):
        return 0
    else:
        for num_add in range(len(txt)):
            new_string = txt + txt[num_add:0:-1] + txt[0]
            if (is_palindrome(new_string)):
                return num_add + 1

