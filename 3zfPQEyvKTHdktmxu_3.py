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
    best_sum = 0
    best_start, best_end = 0, 0
    cur_sum = 0
    for cur_end, x in enumerate(lst):
        if cur_sum <= 0:
            cur_start = cur_end
            cur_sum = x
        else:
            cur_sum += x
        if cur_sum >= best_sum:
            best_sum = cur_sum
            best_start = cur_start
            best_end = cur_end
    return [best_sum, best_start, best_end]

