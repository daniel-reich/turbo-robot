"""


Write a function that divides a list into chunks such that the sum of each
chunk is `<= n`. Start from the left side of the list and move to the right.

### Examples

    divide([1, 2, 3, 4, 1, 0, 2, 2], 5)
    ➞ [[1, 2], [3], [4, 1, 0], [2, 2]]
    
    divide([1, 0, 1, 1, -1, 0, 0], 1)
    ➞ [[1, 0], [1], [1, -1, 0, 0]]
    
    divide([2, 1, 0, -1, 0, 0, 2, 1, 3], 3)
    ➞ [[2, 1, 0, -1, 0, 0], [2, 1], [3]]

### Notes

  * The max of the list will always be smaller than or equal to `n`.
  * Use the **greedy approach** when solving the problem (e.g. fit as many elements you can into a chunk as long as you satisfy the sum constraint).

"""

def divide(numbers, size):
    '''
    Returns a list of lists where each sublist is a contiguous subset of numbers
    such the sum of its elements does not exceed size.
    '''
    groups = []
    current = []
​
    for num in numbers:
        if sum(current) + num <= size:
            current.append(num)
        else:
            groups.append(current)
            current = [num]  # start a new subgroup
​
    if current:
        groups.append(current)  # add last subgroup if it contains numbers
​
    return groups

