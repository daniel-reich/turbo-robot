"""


Create a solution that checks if a given string contains a sub-string pattern
repeated multiple times to return `True` or `False`.

### Examples

    repeated("a") ➞ False
    
    repeated("ababab") ➞ True
    
    repeated("aba") ➞ False
    
    repeated("abcabcabcabc") ➞ True
    
    repeated("aaxxtaaxztaaxxt") ➞ False

### Notes

Adroit programmers can solve this in one line.

"""

def repeated(s):
    if len(s) == 1:
        return False
    for i in range(len(s)//2,0,-1):
         if s.count(s[:i]) > 1 and s.count(s[:i])*len(s[:i]) ==  len(s):
                return True
    return False

