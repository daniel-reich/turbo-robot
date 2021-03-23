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
    max_score = max(s[:-1].count("0") + s[-1].count("1"), s[0].count("0") + s[1:].count("1"))
    for i in range(1, len(s) - 1):
        cnt = s[:i].count("0") + s[i:].count("1")
        max_score = max(max_score, cnt)
    return max_score

