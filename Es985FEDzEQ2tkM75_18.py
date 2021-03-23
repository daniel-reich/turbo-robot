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

def caesar_cipher(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    l = []
    for a in text:
        if a.isalpha():
            l.append(alphabet[(alphabet.index(a) + key) % 26])
        else:
            l.append(a)
    return ''.join(l)

