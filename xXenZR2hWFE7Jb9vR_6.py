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
    lst1 = sorted(set(s), key=lambda c: s.index(c))
    lst2 = sorted(set(t), key=lambda c: t.index(c))
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        pos1 = [idx for idx, c in enumerate(s) if c == lst1[i]]
        pos2 = [idx for idx, c in enumerate(t) if c == lst2[i]]
        if pos1 != pos2:
            return False
    return True

