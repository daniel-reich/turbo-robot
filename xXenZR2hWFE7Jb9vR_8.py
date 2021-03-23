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
    def r(s):
        x = sorted(list(set(list(s))),key=lambda x:s.index(x))
        obj = {}
        for char,i in enumerate(x):
            obj[i]=char
        return  obj
    s1 = r(s)
    t1 = r(t)
    return ''.join(list(map(lambda x:str(s1[x]),list(s)))) ==(''.join(list(map(lambda x:str(t1[x]),list(t)))))

