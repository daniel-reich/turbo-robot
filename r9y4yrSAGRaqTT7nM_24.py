"""


Create a function that takes a list of lists and return the length of the
missing list.

### Examples

    find_missing([[1], [1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]) ➞ 3
    
    find_missing([[5, 6, 7, 8, 9], [1, 2], [4, 5, 1, 1], [1]]) ➞ 3
    
    find_missing([[4, 4, 4, 4], [1], [3, 3, 3]]) ➞ 2

### Notes

  * Test input lists won't always be sorted in order of length.
  * If the list of lists is `None` or empty, your function should return `False`.
  * If a list within the parent list is `None` or empty, return `False`.
  * There will always be a missing element and its length will be between the given lists.

"""

def find_missing(lst):
    if lst == None:
        return False
    else:
        lst.sort(key=len)
    if len(lst) == 0:
        return False
        quit();
    elif len(lst[0]) == 0:
        return False
    else:
        count = len(lst[0])
    for list in lst:
        if count != len(list):
            return count
        count += 1

