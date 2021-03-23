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
    c=''
    for i in range(len(s)):
        a=s[i];b=t[i]
        if s.count(a)!=t.count(b):
            return False
        if a not in c or b not in c:
            c+=a+b+chr(32)
        else:
            if a+b not in c and b+a not in c:
                return False
    return True

