"""


Create a function that takes in a nested list and an element and returns the
frequency of that element by nested level.

### Examples

    freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1)
    ➞ [[0, 1], [1, 2], [2, 3]]
    # The list has one 1 at level 0, 2 1's at level 1, and 3 1's at level 2.
    
    freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5)
    ➞ [[0, 3], [1, 4], [2, 0]]
    
    freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2)
    ➞ [[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]]

### Notes

  * Start the default nesting (a list with no nesting) at 0.
  * Output the nested levels in order (e.g. 0 first, then 1, then 2, etc).
  * Output 0 for the frequency if that particular level has no instances of that element (see example #2).

"""

def helper_freq_count(lst, el, recursive_level, freq_lst):
    """
    go through every element and recursively call this func
    """
    if len(freq_lst) < recursive_level + 1:
        freq_lst.append([recursive_level, 0])
​
    instances = 0
    for i in lst:
        if i == el: #every element found
            instances += 1
        if isinstance(i, list): #if it's a list, recurse
            freq_lst = helper_freq_count(i, el, recursive_level+1, freq_lst)
​
    freq_lst[recursive_level][1] += instances
​
    return freq_lst
​
def freq_count(lst, el):
    return helper_freq_count(lst, el, 0, [])

