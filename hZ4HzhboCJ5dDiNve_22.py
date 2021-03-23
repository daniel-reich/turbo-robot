"""


Create a function that takes a string and returns the reversed string. However
there's a few rules to follow in order to make the challenge interesting:

  * The UPPERCASE/lowercase positions must be kept in the same order as the original string (see example #1 and #2).
  * Spaces must be kept in the same order as the original string (see example #3).

### Examples

    special_reverse_string("Edabit") ➞ "Tibade"
    
    special_reverse_string("UPPER lower") ➞ "REWOL reppu"
    
    special_reverse_string("1 23 456") ➞ "6 54 321"

### Notes

N/A

"""

def special_reverse_string(txt):
    idx = 0
    arr_txt = []
    arr_idx = []
    for i in txt:
        if i != ' ':
            arr_txt.append(i)
        else:
            arr_idx.append(idx)
        idx += 1
​
    arr_txt_lower = []
    for i in arr_txt:
        if i.isalpha():
            arr_txt_lower.append(i.lower())
        else:
            arr_txt_lower.append(i)
        
    arr_reverse = arr_txt[::-1]
    arr = []
    for i, j in zip(arr_reverse, arr_txt):
        if j.isalpha() and j.isupper():
            arr.append(i.upper())
        else:
            arr.append(i.lower())
​
    for i in arr_idx:
        arr.insert(i, ' ')
​
    string = ('').join(arr)
    
    return string

