"""


Create a function that takes a list and returns the sum of all the items in
that list.

### Examples

    sum_list([1, 2, 3]) ➞ 6
    # 1 + 2 + 3 = 6
    
    sum_list([1, [2, [1]], 3]) ➞ 7
    # 1 + 2 + 1 + 3 = 7

### Notes

  * An item in the list can be another list.
  * Try solving it in a recursive approach without using the built-in `sum()` function.

"""

def sum_list(lst):
    if len(lst) == 0:
        return 0
    x = lst.pop()
    if type(x) == list:
        x = sum_list(x)
    return sum_list(lst)+x

