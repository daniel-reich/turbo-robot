"""
Given a column title as it appears in an Excel sheet return its corresponding
column number.

The number is computed in the following way:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

### Examples

    title_to_number("A") ➞ 1
    
    title_to_number("R") ➞ 18
    
    title_to_number("AB") ➞ 28

### Notes

  * `1 <= len(s) <= 7`
  * `s` consists only of uppercase English letters.

"""

def title_to_number(s):
    r = 0
    s = s[::-1]
    for i in range(len(s)):
        if i == 0:
            r += (ord(s[0]) - 64)
        else:
            r += (ord(s[i]) - 64) * 26**i
    return r

