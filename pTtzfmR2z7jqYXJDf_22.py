"""


Create a function that determines whether it is possible to build a palindrome
from the characters in a string.

### Examples

    possible_palindrome("acabbaa") ➞ True
    # Can make the following palindrome: "aabcbaa"
    
    possible_palindrome("aacbdbc") ➞ True
    # Can make the following palindrome: "abcdcba"
    
    possible_palindrome("aacbdb") ➞ False
    
    possible_palindrome("abacbb") ➞ False

### Notes

N/A

"""

def possible_palindrome(txt):
    txt_lst = list(txt)
    txt_set = list(set(txt))
    count_odd = 0
    
    for i in txt_set:
        if txt_lst.count(i) % 2 != 0:
            count_odd += 1
    if count_odd > 1:
        return False
    else:
        return True

