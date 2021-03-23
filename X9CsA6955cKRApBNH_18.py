"""


A **consecutive-run** is a list of adjacent, consecutive integers. This list
can be either increasing or decreasing. Create a function that takes a list of
numbers and returns the length of the longest **consecutive-run**.

To illustrate:

    longestRun([1, 2, 3, 5, 6, 7, 8, 9]) ➞ 5
    # Two consecutive runs: [1, 2, 3] and [5, 6, 7, 8, 9] (longest).

### Examples

    longest_run([1, 2, 3, 10, 11, 15]) ➞ 3
    # Longest consecutive-run: [1, 2, 3].
    
    longest_run([5, 4, 2, 1]) ➞ 2
    # Longest consecutive-run: [5, 4] and [2, 1].
    
    longest_run([3, 5, 7, 10, 15]) ➞ 1
    # No consecutive runs, so we return 1.

### Notes

If there aren't any consecutive runs (there is a gap between each integer),
return `1`.

"""

def longest_run(numbers):
    '''
    Returns the length of the longest consecutive run in numbers, where a run is
    a sequence of integers differing either by 1 (ascending) or -1 (descending).
    '''
    from operator import add, sub
    
    max_count = 1
    size = len(numbers)
​
    for op in(add, sub):
        i = j = 0
        count = 1
        
        while i < size-1:
            while j < size-1 and op(numbers[j], 1) == numbers[j+1]:
                count += 1
                j+= 1
            if count > max_count:
                max_count = count
            i, j = j, j+1
            count = 1
    
    return max_count

