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

def rotated_words(txt):
    rotate_letters = ["H", "I", "N", "M", "O", "S", "W", "X", "Z"]
    words = set(txt.split())
    full_rot_words = 0
    for w in words:
        rotated_letters = 0
        for x in w:
            if x.upper() in rotate_letters:
                rotated_letters += 1
        if len(w) == rotated_letters:
            full_rot_words += 1
    return full_rot_words

