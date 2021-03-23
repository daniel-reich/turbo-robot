"""


Given a list of _10 numbers_ , return whether or not the list is shuffled
sufficiently enough. In this case, if **3 or more** numbers appear
**consecutively** (ascending or descending), return `False`.

### Examples

    is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]) ➞ False
    # 1, 2, 3 appear consecutively
    
    is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]) ➞ False
    # 9, 8, 7, 6 appear consecutively
    
    is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]) ➞ True
    # No consecutive numbers appear
    
    is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) ➞ True
    # No consecutive numbers appear

### Notes

  * Only steps of 1 in either direction count as consecutive (i.e. a sequence of odd and even numbers would count as being properly shuffled (see example #4)).
  * You will get numbers from 1-10.

"""

def is_shuffled_well(lst):
    count_up, count_down = 0, 0
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] + 1:
            count_up += 1
            count_down = 0
        elif lst[i] == lst[i - 1] - 1:
            count_down += 1
            count_up = 0
        else:
            count_up, count_down = 0, 0
        if count_up == 2 or count_down == 2:
            return False
    return True

