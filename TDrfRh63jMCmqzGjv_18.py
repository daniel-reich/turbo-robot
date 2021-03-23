"""


Given two lists, return whether the two lists are opposites of each other.
That means both lists are comprised only from elements `a` and `b` and the
occurrences of these elements are swapped between the two lists.

### Examples

    is_anti_list(["1", "0", "0", "1"], ["0", "1", "1", "0"]) ➞ True
    
    is_anti_list(["apples", "bananas", "bananas"], ["bananas", "apples", "apples"]) ➞ True
    
    is_anti_list([3.14, True, 3.14], [3.14, False, 3.14]) ➞ False

### Notes

All tests will include only two different elements.

"""

def is_anti_list(lst1, lst2):
    if lst1[0] != lst2[0] and lst1[1] != lst2[1]:
        pairs = {lst1[0]: lst2[0], lst1[1]: lst2[1]}
        for i in range(2, len(lst1)):
            if lst1[i] != pairs[lst2[i]]:
                return False
        return True
    return False

