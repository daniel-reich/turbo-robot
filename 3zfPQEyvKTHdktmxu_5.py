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
    mss = [-float('inf')]
    start = 0
    current = 0
​
    for i, x in enumerate(lst):
        current = max(current+x, 0)
        if not current:
            start = i + 1
        if current >= mss[0]:
            mss = [current, start, i]
    
    return mss

