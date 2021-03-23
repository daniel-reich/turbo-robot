"""


Create a function which adds _zeros_ to the **start** of a binary string, so
that its length is a **mutiple of 8**.

### Examples

    complete_binary("1100") ➞ "00001100"
    
    complete_binary("1101100") ➞ "01101100"
    
    complete_binary("110010100010") ➞ "0000110010100010"

### Notes

Return the same string if its length is already a multiple of 8.

"""

def complete_binary(s): #w/o built-in
    def l(st):
        c = 0
        while st:
            c += 1
            st = st[1:]
        return c
    s = s[::-1]
    while l(s) % 8:
        s += "0"
    return s[::-1]

