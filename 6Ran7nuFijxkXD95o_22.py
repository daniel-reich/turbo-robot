"""


Given a sentence containing few instances of `"Ctrl + C"` and `"Ctrl + V"`,
return the sentence after those keyboard shortcuts have been applied! Note
that:

  * In this case, `"Ctrl + C"` will copy **all text** behind it.
  * In this case, `"Ctrl + V"` will do nothing if there is no `"Ctrl + C"` before it.
  * A `"Ctrl + C"` which follows another `"Ctrl + C"` will overwrite what it copies.

### Examples

    keyboard_shortcut("the egg and Ctrl + C Ctrl + V the spoon") ➞ "the egg and the egg and the spoon"
    
    keyboard_shortcut("WARNING Ctrl + V Ctrl + C Ctrl + V") ➞ "WARNING WARNING"
    
    keyboard_shortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V") ➞ "The The Town The The Town"

### Notes

  * Keyboard shortcut commands will appear like normal words in a sentence but shouldn't be copied themselves (see example #2).
  * Pasting should add a space between words.

"""

from re import sub
length = len("Ctrl + C ")
def keyboard_shortcut(txt,copied = None):
  while True:
    if not "Ctrl +" in txt:
      return sub(r'\s{2,}|\s+$','',txt)
    index = txt.index("Ctrl +")
    if txt[index+7] == "C":
      copied = txt[:index]
      txt = txt[:index] + txt[index+length::]
    else:
      if copied:
        txt = txt[:index] + copied + txt[index+length::]
      else:
        txt = txt[:index] + txt[index+length::]

