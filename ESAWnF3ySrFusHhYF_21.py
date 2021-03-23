"""


Create a function that takes a list of any _length_. Modify each element
**(capitalize, reverse, hyphenate)**.

### Examples

    edit_words(["new york city"]) ➞ ["YTIC KR-OY WEN"]
    
    edit_words(["null", "undefined"]) ➞ ["LL-UN", "DENIF-EDNU"]
    
    edit_words(["hello", "", "world"]) ➞ ["OLL-EH", "-", "DLR-OW"]
    
    edit_words([""]) ➞ ["-"]

### Notes

Input list values can be any _type_.

"""

def edit_words(arr):
    x = [j[::-1] for j in [i.upper() for i in arr]]
    y = [i[:len(i)//2]+'-'+i[len(i)//2:] if len(i) %
         2 == 0 else i[:len(i)//2+1]+'-'+i[len(i)//2+1:] for i in x]
​
    return y

