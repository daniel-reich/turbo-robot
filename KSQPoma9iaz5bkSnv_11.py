"""


Given a number `n`, return a list containing several lists. Each list
increment in size, from range `1 to n inclusive`, contaning its length as the
elements.

### Examples

    pyramid_lists(1) ➞ [[1]]
    
    pyramid_lists(3) ➞ [[1], [2, 2], [3, 3, 3]]
    
    pyramid_lists(5) ➞ [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5]]

### Notes

`n` will be a positive integer.

"""

def pyramid_lists(n):
    n_range = list(range(1, n + 1))
    output = []
    for list_values in n_range:
        list_length = []
        for thing in range(list_values):
            list_length.append(list_values)
        output.append(list_length)
    return output

