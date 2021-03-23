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

def kadane(A):
    maxSoFar = 0
    maxEndingHere = 0
    start = end = 0
    beg = 0
    for i in range(len(A)):
        maxEndingHere = maxEndingHere + A[i]
        if maxEndingHere < 0:
            maxEndingHere = 0
            beg = i + 1
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
            start = beg
            end = i
    return [maxSoFar, start, end]
​
def big_sub(lst):
    ans = kadane(lst)
    if ans[0] == max(lst):
        for i in range(len(lst) - 1, -1, -1):
            if lst[i] == ans[0]:
                return [ans[0], i, i]
    return kadane(lst)

