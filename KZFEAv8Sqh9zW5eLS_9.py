"""


A list that represents a **Binary Tree** is in the following form:

    binary_tree = [val, lst_left, lst_right]

When `lst_left` is the left side of the tree and `lst_right` is the right side
of the tree.

To illustrate:

    list1 = [3, [ 8, [ 5, None, None], None], [ 7, None, None]]
    
    # list1 represents the following Binary Tree:
    
                        3
                       / \
                      8   7
                     /\   /\
                    5  N N  N
                   /\
                   N N
    
    # While N represents None.

Create a function that takes a list that represent a Binary Tree and a value
and return `True` if the value is in the tree and, `False` otherwise.

### Examples

    is_val_in_tree(list1, 5) ➞ True
    
    is_val_in_tree(list1, 9) ➞ False
    
    is_val_in_tree(lst2, 51) ➞ False

### Notes

The tree will contain integers only and will be presented by a list in the
specified format.

"""

def is_val_in_tree(tree, val):
    return str(val) in str(tree)

