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
  return [False if diff(word, txt) > 2 else True for word in lst]
      
​
def diff(test_word, ideal_word):
  if len(test_word) != len(ideal_word) or set(test_word) != set(ideal_word):
    return 3
  else:
    count = 0
    for a in range(len(test_word)):
      if test_word[a] != ideal_word[a]:
        count += 1
      if count > 2:
        return count
    return count

