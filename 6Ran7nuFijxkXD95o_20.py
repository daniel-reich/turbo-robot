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

def keyboard_shortcut(txt):
    txt_split = txt.split()
    result = []
    to_copy = ''
    for i in range(len(txt_split)):
        if txt_split[i] == "Ctrl" and txt_split[i+1] == "+" and  txt_split[i+2] == "C":
            to_copy = ""
            for j in range(0, i):
                if txt_split[j] != "Ctrl" and txt_split[j] != "+" and txt_split[j] != "C" and txt_split[j] != "V":
                    to_copy += txt_split[j] + " "
            txt_split[i] = to_copy.rstrip()
        elif txt_split[i] == "Ctrl" and txt_split[i+1] == "+" and  txt_split[i+2] == "V" and to_copy != "":
              result.append(to_copy.rstrip())
              to_copy = ''
        elif txt_split[i] != "Ctrl" and txt_split[i] != "+" and  txt_split[i] != "C" and txt_split[i] != "V":
            result.append(txt_split[i])
    return " ".join(result)

