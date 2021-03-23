"""


Create a function that takes two arguments (`text`, `key`) and returns a new
encrypted text using the `key`. For example, if the input is `"a"` and the key
is `1`, it should move that letter 1 step in alphabetic order so the output
would be `"b"`.

### Examples

    caesar_cipher("hello", 5) ➞ "mjqqt"
    
    caesar_cipher("hello world", 1) ➞ "ifmmp xpsme"
    
    caesar_cipher("a", 2) ➞ "c"

### Notes

The input is only letters and spaces; no special characters.

"""

def g(c, a, key):
    x = ord(c) - ord(a)
    y = (x + key) % 26
    return chr(ord(a) + y)
​
def f(c, key): #c:chr
    if 'a' <= c <= 'z':
        return g(c, 'a', key)
    elif 'A'<= c <= 'Z':
        return g(c, 'A', key)
    return c
​
def caesar_cipher(a, key):
    return ''.join(f(x, key) for x in a)

