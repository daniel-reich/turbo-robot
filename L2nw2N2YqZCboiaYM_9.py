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
    n = len(s)
    if n == 1:
        return False
    for k in range(1, n):
        if n % k == 0 and s == s[:k] * (n // k):
            return True
    return False

