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

def validate_swaps(lst, txt):
    bool_list=[]
​
    for i in range(len(lst)):
​
        if len(txt) != len(lst[i]):
            bool_list.append(False)
            continue
        times_swapped = 0
        if set(lst[i]) & set(txt) == set(lst[i]) :
            for j in range(len(lst[i])):
                if lst[i][j]!=txt[j]:
                    times_swapped+=1
            if times_swapped == 2:
                bool_list.append(True)
            else:
                bool_list.append(False)
​
        else:
            bool_list.append(False)
    return bool_list

