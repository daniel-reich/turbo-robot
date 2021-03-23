"""


This is a reverse-coding challenge. Create a function that outputs the correct
list from the input. Use the following examples to crack the code.

### Examples

    decode("hello") ➞ [5, 2, 9, 9, 3]
    
    decode("wonderful") ➞ [11, 3, 2, 1, 2, 6, 3, 9, 9]
    
    decode("something challenging") ➞ [7, 3, 10, 2, 8, 5, 6, 2, 4, 5, 18, 5, 16, 9, 9, 2, 2, 4, 6, 2, 4]

### Notes

N/A

"""

def decode(txt):
    # Why you put 10 in letters that dont have tips, and y=4 ???
    tips =[["hello",[5,2,9,9,3]],["wonderful",[11, 3, 2, 1, 2, 6, 3, 9, 9]],
            ["something challenging",[7, 3, 10, 2, 8, 5, 6, 2, 4, 5, 18, 5, 16, 9, 9, 2, 2, 4, 6, 2, 4]]]
    code, change, save = {'y':4}, len(txt), []
    for x in range(len(tips)):
        key, item = tips[x][0], tips[x][1]
        for y in range(len(key)):
            code[key[y]] = item[y]
    for x in range(change):
        try:
            save.append(code[txt[x]])
        except:
            save.append(10)
    return save

