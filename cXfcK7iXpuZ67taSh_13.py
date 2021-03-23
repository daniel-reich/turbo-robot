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
    retstr = ""
    while txt != '':
        num = ""
        i = 1
        np = 1
        bu = txt[0]
        while i < len(txt) and ord(txt[i]) >= 48 and ord(txt[i]) < 58:
            num += txt[i]
            i += 1
            np += 1
        num = int(num)
        for x in range(num):
            retstr += bu
        txt = txt[np::]
    return retstr

