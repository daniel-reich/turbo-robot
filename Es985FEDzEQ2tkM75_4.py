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
    RESULT = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(len(alphabet))
    
    for elem in list(str(text)):
        if elem in list(alphabet):
            POSITION = alphabet.find(elem)
            key2 = alphabet.find(elem) + key
            if key2 > 25:
                key2 = key2 - 26
                print(key2, RESULT, alphabet.find(elem) + key )
            RESULT.append(list(alphabet)[key2])
        else:
            RESULT.append(' ')
    
    
    print(''.join(RESULT))
    return ''.join(RESULT)
    
caesar_cipher("iwxh xh p rwxetg", 11)

