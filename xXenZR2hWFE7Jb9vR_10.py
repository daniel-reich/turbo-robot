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
    if True:    # to lazy to un-indent from LeetCode solution:
        forw_mapping = {}
        rev_mapping = {}
        if len(s) != len(t):
            return False
        n = len(s)
        for i in range(n):
            cs, ct = s[i], t[i]
            if cs in forw_mapping:
                if forw_mapping[cs] != ct:
                    return False
            else:
                if ct in forw_mapping.values():
                    return False
                forw_mapping[cs] = ct
                rev_mapping[ct] = cs
            if ct in rev_mapping:
                if rev_mapping[ct] != cs:
                    return False
            else:
                if cs in rev_mapping.values():
                    return False
                rev_mapping[ct] = cs
        return True

