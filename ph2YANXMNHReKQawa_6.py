"""


Create a function that takes a range object `r`, index `i`, and returns a list
where the first element is the **number of elements** in the range object, and
the second element is the **element of the range object at the given index**.

### Examples

    length_element(range(2, 4), 0) ➞ [2, 2]
    
    length_element(range(12, 15, 2), 1) ➞ [2, 14]
    
    length_element(range(40, 50, 3), 2) ➞ [4, 46]

### Notes

No need to check for `IndexError`.

"""

def length_element(r, i):
  return [len(list(r)), list(r)[i] ]

