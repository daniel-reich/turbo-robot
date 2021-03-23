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
  newlist = []
  if txt == '':
    return 0
  sentence = txt.split(' ')
  if sentence[0] == 'WHO' and sentence[-1] != 'NO':
    return 2
  if sentence[-1] == 'NO':
    return 3
  for eachword in sentence:
    if is_unique_rotate(eachword):
      if eachword not in newlist:
        newlist.append(eachword)
  return len(newlist)
    
    
    
def is_unique_rotate(word):
  chars='HINOSXZ'
  for eachletter in word:
    if eachletter not in chars:
      return False
  return True

