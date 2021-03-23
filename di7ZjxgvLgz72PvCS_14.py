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
    holder = []
    while lst:
        to_eval = list(lst.pop(0))
        for char in range(len(to_eval) - 1):
            for i in range(char, len(to_eval)):
                new = to_eval.copy()
                new[char], new[i] = new[i], new[char]
                if "".join(new) == txt: 
                    holder.append(True)
                    break
            else:
                continue  
            break
        else:
            holder.append(False)
    return holder

