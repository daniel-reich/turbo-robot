"""


Some characters do not change after a rotation of 180 degrees. They can be
read, although sometimes in a different way. For example, uppercase letters
**"H", "I", "N", "O", "S", "X", "Z"** after rotation are not changed, the
letter **"M" becomes a "W", and vice versa.**

So, the word **"WOW"** turns into the word **"MOM"**. On the other hand, the
word **"HOME"** cannot be rotated.

Find the number of unique readable **Rotated Words** in the input string `txt`
(without duplicates).

### Examples

    rotated_words("HSSN") ➞ 1
    # String can be rotated to a valid string
    
    rotated_words("OS IS UPDATED") ➞ 2
    # "OS" and "IS" can be rotated to a valid string
    
    rotated_words("MUBASHIR") ➞ 0

### Notes

String contains only uppercase letters.

"""

def check(w):
    for i in w:
        if i not in ["H", "I", "N", "O", "S", "X", "Z","W","M"]:return False
    return 1
​
def rotated_words(txt):
    return list(map(check,set(txt.split(" ")))).count(1) if  txt else 0

