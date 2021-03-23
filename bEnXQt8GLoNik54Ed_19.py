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
    ones = s.count("1")
    start = -(s[0]=="1") + ones + (s[0]=="0")
    mini = start
    for i in s[1:-1]:
        if i == "0":
            start += 1
        else:
            start -= 1
        if start > mini:
            mini = start
    return mini

