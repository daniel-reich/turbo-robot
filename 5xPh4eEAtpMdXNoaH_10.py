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
    length = len(s)
    if length <= 1:
        return length
    ans = 2 * sum([s.count(i)//2 for i in set(s) if s.count(i) > 1])
    if ans == length:
        return length
    else:
        return ans + 1

