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

def mystery_func(n):
    i = 0
    j = 0
    lst = []
    while j < n:
        j = 2**i
        lst.append(j)
        i +=1
    return int(str("2"*(len(lst)-2))+str(n-lst[len(lst)-2]))

