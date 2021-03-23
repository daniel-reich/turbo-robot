"""


This is a **reverse coding challenge**. Normally you're given explicit
directions with how to create a function. Here, you must generate your own
function to satisfy the relationship between the inputs and outputs.

Your task is to create a function that, when fed the inputs below, produce the
sample outputs shown.

### Examples

    3 ➞ 21
    
    9 ➞ 2221
    
    17 ➞ 22221
    
    24 ➞ 22228

### Notes

If you get stuck, check the **Comments** for help.

"""

def mystery_func(num):
    i = 0
    while True:
        if 2**i > num:
            break
        else:
            i += 1
    i -= 1
    rem = num - 2**i
    res = ""
    for j in range(0, i):
        res += "2"
    res += str(rem)
    return int(res)

