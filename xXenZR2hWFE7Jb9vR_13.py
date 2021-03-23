"""


Given two strings `s` and `t`, create a function to determine if they are
isomorphic. Two strings are isomorphic if the characters in `s` can be
replaced to get `t`. All occurrences of a character must be replaced with
another character while preserving the order of characters. No two characters
may map to the same character but a character may map to itself.

### Examples

    is_isomorphic("egg", "add") ➞ True
    
    is_isomorphic("aba", "baa") ➞ False
    
    is_isomorphic("paper", "title") ➞ True

### Notes

N/A

"""

def is_isomorphic(s, t):
    d1, d2 = {}, {}
    for a, b in zip(s, t):
        if a in d1 and d1[a] != b:
            return False
        d1[a] = b
        if b in d2 and d2[b] != a:
            return False
        d2[b] = a
    return True

