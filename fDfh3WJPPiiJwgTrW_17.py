"""


Return the total number of lists inside a given list.

### Examples

    num_of_sublists([[1, 2, 3]]) ➞ 1
    
    num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) ➞ 3
    
    num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]) ➞ 4
    
    num_of_sublists([1, 2, 3]) ➞ 0

### Notes

N/A

"""

def num_of_sublists(lst):
    return sum(isinstance(i, list) for i in lst)

