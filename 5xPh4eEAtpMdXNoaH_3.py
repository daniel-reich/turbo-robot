"""


Given a string `s`, return the length of the longest palindrome that can be
built with those letters.

### Examples

    longest_palindrome("a") ➞ 1
    
    longest_palindrome("bb") ➞ 2
    
    longest_palindrome("abccccdd") ➞ 7
    
    longest_palindrome("") ➞ 0

### Notes

N/A

"""

from collections import Counter
​
def longest_palindrome(s):
    C = Counter(s)
    ans = 0
    odd = False
    for c in C.values():
        if c % 2 == 0:
            ans += c
        else:
            ans += c - 1
            odd = True
    return ans + (1 if odd else 0)

