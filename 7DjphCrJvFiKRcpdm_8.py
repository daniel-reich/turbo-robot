"""


Write a function that returns the total number of **integers** covered from a
list of intervals ( **inclusive** ). In other words, return the number of
different integers in the lists.

### Examples

    covered_integers([[80, 81], [1, 2], [9, 11]]) ➞ 7
    # Seven integers are covered: 1, 2, 9, 10, 11, 80, 81
    
    covered_integers([[3, 6], [4, 6], [5, 6]]) ➞ 4
    
    covered_integers([[1, 2], [1, 2]]) ➞ 2

### Notes

  * Intervals may overlap, be subintervals of each other, or be identical.
  * For each interval `[l, u]`, `l` and `u` will be integers, and `l <= u` will always be true.

"""

def covered_integers(lst):
    lst_new = []
    ([[lst_new.append(b) for b in range(a[0], a[1]+1)] for a in lst])
    return len(set(lst_new))

