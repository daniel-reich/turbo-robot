"""


A list is **special** if every **even index** contains an **even number** and
every **odd index** contains an **odd number**. Create a function that returns
`True` if an array is **special** , and `False` otherwise.

### Examples

    is_special_array([2, 7, 4, 9, 6, 1, 6, 3]) ➞ True
    # Even indices: [2, 4, 6, 6]; Odd indices: [7, 9, 1, 3]
    
    is_special_array([2, 7, 9, 1, 6, 1, 6, 3]) ➞ False
    # Index 2 has an odd number 9.
    
    is_special_array([2, 7, 8, 8, 6, 1, 6, 3]) ➞ False
    # Index 3 has an even number 8.

### Notes

N/A

"""

def is_special_array(lst):
    should_be_even = False
    for num in lst:
        if num % 2 != should_be_even:
            return False
        should_be_even = not should_be_even
    return True

