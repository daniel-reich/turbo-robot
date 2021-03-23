"""


Say you want to traverse a list of integers starting at the first item and
using each value as a pointer of what item to visit next. For example, you
would traverse the list `[1, 4, 3, 0, 2]` in the following manner:

![List](https://edabit-challenges.s3.amazonaws.com/gAbF8Rs.png)

Because you visit every item once and go back to the starting point, the list
`[1, 4, 3, 0, 2]` is a "full cycle".

Create a function that returns `True` if the input list is a full cycle, or
`False` otherwise.

### Examples

    full_cycle([1, 4, 3, 0, 2]) ➞ True
    
    full_cycle([1, 4, 0, 3, 2]) ➞ False
    
    full_cycle([5, 3, 4, 2, 0, 1]) ➞ True

### Notes

Test lists won't include any negative integers.

"""

def full_cycle(lst):
​
    dict_1, dict_2 = {}, {}
    curr_val, next_ind = lst[0], lst[0]
​
    if max(lst)> len(lst) - 1:
            return False
​
    for i in range(max(lst) + 1):
        dict_1[str(i)] = 1
        dict_2[str(i)] = 0
        if lst.count(lst[i]) > 1:
            return False
        
    while next_ind != 0:
        if max(dict_2.values()) > 1:
            return False
        dict_2[str(curr_val)] += 1
        next_ind = curr_val
        curr_val = lst[next_ind]
​
    return dict_1 == dict_2

