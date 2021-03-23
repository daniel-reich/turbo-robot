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

import re
def keyboard_shortcut(txt):
    typed = ""
    copied = ""
    txt = re.sub(r'Ctrl \+ C', '&', txt)
    txt = re.sub(r'Ctrl \+ V', '$', txt)
​
    for i in txt:
        if i == "&":
            copied = typed
        elif i == "$":
            typed += copied
        else:
            typed += i
            
    typed = re.sub(r'\s+', ' ', typed)
    return typed.strip()

