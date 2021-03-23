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
    a = []
    for word in lst:
        
        word = list(word)
​
        if len(word) != len(txt):
            a.append(False)
            continue
        
        for letter in word:
            your_letter = word.index(letter)
            belongs = txt.find(letter)
            
            if your_letter != belongs:
                break
        
        if belongs < 0:
            a.append(False)
            continue
​
        word[your_letter], word[belongs] = word[belongs], word[your_letter]
​
        if word == list(txt):
            a.append(True)
        else:
            a.append(False)
    
    return a

