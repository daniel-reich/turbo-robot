"""


Given an array of strings and an original string, write a function to output
an array of boolean values - `True` if the word can be formed from the
original word by swapping two letters **only once** and `False` otherwise.

### Examples

    validate_swaps(["BACDE", "EBCDA", "BCDEA", "ACBED"], "ABCDE")
    ➞ [True, True, False, False]
    
    # Swap "A" and "B" from "ABCDE" to get "BACDE".
    # Swap "A" and "E" from "ABCDE" to get "EBCDA".
    # Both "BCDEA" and "ACBED" cannot be formed from "ABCDE" using only a single swap.
    
    validate_swaps(["32145", "12354", "15342", "12543"], "12345")
    ➞ [True, True, True, True]
    
    validate_swaps(["9786", "9788", "97865", "7689"], "9768")
    ➞ [True, False, False, False]

### Notes

Original string will consist of unique characters.

"""

def swap(strg,i1,i2):
    strlist = []
    for char in strg: 
        strlist.append(char) 
    temp = strlist[i1]
    strlist[i1] = strlist[i2]
    strlist[i2] = temp
    joined = "".join(strlist)
    return joined 
​
def validate_swaps(lst, txt):
    boolst = []
    word = "No!"
    for strg in lst: 
        word = "No!"
        for i in range(len(strg)): 
            for j in range(i+1,len(strg)):
                swappedstr = ""
                if i != j: 
                    swappedstr = swap(strg,i,j)
                if swappedstr == txt: 
                    boolst.append(True)
                    word ="Yes!"
                    break
            if word == "Yes!":
                break 
        if word == "No!":
            boolst.append(False) 
    return boolst

