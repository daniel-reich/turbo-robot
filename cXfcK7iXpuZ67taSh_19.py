"""


This is a **reverse coding challenge**. Normally you're given explicit
directions with how to create a function. Here, you must generate your own
function to satisfy the relationship between the inputs and outputs.

Your task is to create a function that, when fed the inputs below, produce the
sample outputs shown.

### Examples

    "A4B5C2" ➞ "AAAABBBBBCC"
    
    "C2F1E5" ➞ "CCFEEEEE"
    
    "T4S2V2" ➞ "TTTTSSVV"
    
    "A1B2C3D4" ➞ "ABBCCCDDDD"

### Notes

If you get stuck, check the **Comments** for help.

"""

def mystery_func(txt):
    a = []
    newString = ""
    for char in txt:
        if char.isdigit() is True:
            a.append(int(char))
        else:
            a.append(char)
    for i in a:
        try:
            if a.index(i) < len(a) and type(a[a.index(i) + 1]) == int:
                add = i * a[a.index(i) + 1]
                newString += str(add)
            else:
                pass
        except:
            pass
    return newString

