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
    r, one = 0, False
    for i in set(s):
        a = s.count(i)
        if a % 2 == 0:
            r += a
        else:
            r += a - 1
            a = 1
        if a == 1 and one == False:
            r += a
            one = True
    return r

