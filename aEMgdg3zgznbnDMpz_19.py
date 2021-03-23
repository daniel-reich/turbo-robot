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
  sp_char = ["H", "I", "N", "O", "S", "W", "X", "Z" ]
  if txt:
    count = 0
    words = set(txt.split(" "))
    print(words)
    for word in words:
      l = 0
      for char in word:
        if char in sp_char:
          l +=1
      if l == len(word):
        count+=1
    return count
  else:
    return 0

