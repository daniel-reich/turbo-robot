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

def longest_palindrome(s):
    p = sum([(1 if i%2 else 0) for i in [s.count(i) for i in set(s)]])
    return len(s) - p + (p != 0)

