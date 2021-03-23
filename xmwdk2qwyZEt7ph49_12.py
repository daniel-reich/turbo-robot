"""


Python's `len()` method will return the number of elements in a list. For
example, the list below contains 2 elements:

    [1, [2, 3]]
    # 2 elements, number 1 and list [2, 3]

Suppose we instead wanted to know the **total number of non-nested items** in
the nested list. In the above case, `[1, [2, 3]]` contains 3 **non-nested
items** , `1`, `2` and `3`.

Create a function that returns the total number of non-nested items in a
nested list.

### Examples

    get_length([1, [2, 3]]) ➞ 3
    
    get_length([1, [2, [3, 4]]]) ➞ 4
    
    get_length([1, [2, [3, [4, [5, 6]]]]]) ➞ 6
    
    get_length([1, [2], 1, [2], 1]) ➞ 5

### Notes

An empty list should return `0`.

"""

def get_length(lst):
  return len([x for x in str(lst) if x.isdigit() == True])

