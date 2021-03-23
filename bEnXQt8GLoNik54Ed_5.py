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
  total = (1 if s[0] == "0" else 0) + sum(s[i] == "1" for i in range(1, len(s)))
  max_total = total
  for i in range(1, len(s)-1):
    total += 1 if s[i] == "0" else -1
    if total > max_total:
      max_total = total
  return max_total

