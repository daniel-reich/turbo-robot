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
    m = 0
    for i in range(len(s)):
        l, r = s[0: i + 1], s[i + 1:]
        if len(l) >= 1 and len(r) >= 1:
            calc = len(l.replace('1', '')) + len(r.replace('0', ''))
            m = calc if calc > m else m
    return m

