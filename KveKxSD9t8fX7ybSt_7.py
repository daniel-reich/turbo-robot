"""


A countdown sequence is a descending sequence of `k` integers from `k` down to
1 (e.g. 5, 4, 3, 2, 1). Write a function that returns a list `[x, y]` where
**x** is the number that represents how many of countdown sequences are in a
given list and **y** is a list of those sequences in order which they appear
in the list.

### Examples

    final_countdown([4, 8, 3, 2, 1, 2]) ➞ [1, [[3, 2, 1]]]
    # In this example we have 1 countdown sequence: 3, 2, 1
    
    final_countdown([4, 4, 5, 4, 3, 2, 1, 8, 3, 2, 1]) ➞ [2, [[5, 4, 3, 2, 1], [3, 2, 1]]]
    # We have 2 countdown sequences:
    # 5, 4, 3, 2, 1 and 3, 2, 1
    
    final_countdown([4, 3, 2, 1, 3, 2, 1, 1]) ➞ [3, [[4, 3, 2, 1], [3, 2, 1], [1]]]
    # We have 3 countdown sequences:
    # 4, 3, 2, 1 ; 3, 2, 1 and 1
    
    final_countdown([1, 1, 2, 1]) ➞ [3, [[1], [1], [2, 1]]]
    
    final_countdown([]) ➞  [0, []]

### Notes

  * `[1]` is a valid countdown sequence.
  * All numbers will be greater than 0.

"""

def final_countdown(lst):
    r = []
    lst = lst[::-1]
    while True:
        if 1 in lst:
            i = lst.index(1)
        else:
            r = r[::-1]
            r = [len(r)] + [r]
            return r
        lst = lst[i:]
        i = 1
        while len(lst) > 1 and lst[i] - 1 == lst[i - 1]:
            i += 1
            if i == len(lst):
                break
        r += [lst[: i][::-1]]
        lst = lst[i :]

