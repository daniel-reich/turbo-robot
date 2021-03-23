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
def longest_palindrome(s):
    one_odd, count = False, 0
    for v in Counter(s).values():
        if v % 2:
            count += v - 1
            if not one_odd:
                one_odd = True
        else:
            count += v
    return count + one_odd

