"""


For a given list, determine the biggest possible sum between consecutive
terms, as well as the initial and final position of the terms.

### Examples

    big_sub([4, -3, 5, -7, 5]) ➞ [6 (sum), 0 (start), 2 (end)]
    
    big_sub([4, -3, -5, 7, 5]) ➞ [12, 3, 4]
    
    big_sub([2, -3, 2, -3, 2]) ➞ [2, 4, 4]

### Notes

  * If the biggest sum is repeated at several intervals, return the starting and ending positions of the latest interval.
  * The list will always have positive numbers.

"""

def big_sub(lst):
    n = len(lst)
    res = [lst[0], 0, 0]
    for r in range(n):
        if lst[r] > 0:
            s = lst[r]
            if s >= res[0]:
                res = [s, r, r]
            for c in range(r + 1, n):
                s += lst[c]
                if s >= res[0]:
                    res = [s, r, c]
    return res

