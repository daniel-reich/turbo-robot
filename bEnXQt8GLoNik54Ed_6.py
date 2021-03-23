"""


Given a string `s` formed from zeros and ones, return the maximum score after
splitting the string into two **non-empty** substrings (`left` and `right`).

The score after splitting a string is the number of zeros in the `left`
substring plus the number of ones in the `right` substring.

### Examples

    max_score("00111") ➞ 5
    # left = "00", right = "111" ➞ 2 + 3 ➞ 5
    
    max_score("1111") ➞ 3
    
    max_score("01001") ➞ 4
    
    max_score("010101010101010101") ➞ 10

### Notes

N/A

"""

def max_score(s):
    if len(s) == 2:
        ans = 1 if s[0] == '0' else 0
        ans += 1 if s[1] == '1' else 0
        return ans
    ans = 0
    for i in range(1, len(s)):
        left, right = s[:i], s[i:]
        ans = max(ans, left.count('0') + right.count('1'))
    return ans

