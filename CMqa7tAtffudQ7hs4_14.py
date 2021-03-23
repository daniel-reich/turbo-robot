"""


Given a shuffled list `l`, return a sequence of _transpositions_ which sorts
the list (as in `sorted(l)`). A transposition is a pair of indices `(i, j)`
representing that `l[i]` and `l[j]` be swapped. Specifically, the output is a
list of transpositions to be applied. Transpositions are applied as in:

    def apply_transpositions(l, swaps):
      for i, j in swaps:
      l[i], l[j] = l[j], l[i]
    return l

### Examples

    sorting_steps([5, -5]) ➞ [(0, 1)]
    # Swap first and second elements.
    
    sorting_steps([4, 3, 2, 1]) ➞ [(0, 3), (1, 2)] or even [(0, 1), (1, 2), (2, 3), (0, 1), (1, 2), (0, 1)]
    
    sorting_steps([6, 6]) ➞ []

### Notes

Output is not unique! A given list may be sorted with varying numbers of
transpositions stemming from various sorting techniques. You need only produce
output which works. (This gives the problem algorithimic freedom!)

"""

def sorting_steps(items):
    '''
    Returns the item swaps needed to sort the elements in items as described
    above.
    '''
    from copy import deepcopy
    tester = deepcopy(items)  # so don't affect original
    steps = []
​
    # Select the steps necessary to perform a bubble sort
    for i in range(len(items) - 1):
        for j in range(len(items) - i - 1):
            if tester[j] > tester[j+1]:
                tester[j], tester[j+1] = tester[j+1], tester[j]
                steps.append((j,j+1)) # add the swap
​
    return steps

