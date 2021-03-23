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
    if type(s) != str or type(t) != str:
        return False
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] in s[:i]:
            continue
        elif s.count(s[i]) == 1:
            continue
        elif s.count(s[i]) > 1:
             cnt = s.count(s[i]) - 1
             index = s.find(s[i], i + 1, len(s))
             while cnt > 0:
                 if t[index] != t[i]:
                      return False
                 else:
                     cnt -= 1
                     index = s.find(s[i], index +1, len(s))
    for i in range(len(t)):
        if t[i] in t[:i]:
            continue
        elif t.count(t[i]) == 1:
            continue
        elif t.count(t[i]) > 1:
            cnt = t.count(t[i]) - 1
            index = t.find(t[i], i + 1, len(t))
            while cnt > 0:
                if s[index] != s[i]:
                    return False
                else:
                    cnt -= 1
                    index = t.find(t[i], index + 1, len(t))
​
    return True

