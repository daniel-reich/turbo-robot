"""


Create a function that takes a list `lst` and a number `n` and returns a list
of two integers whose product is that of the number `n`.

### Examples

    two_product([1, 2, 3, 4, 13, 5], 39) ➞ [3, 13]
    
    two_product([11, 2, 7, 3, 5, 0], 55) ➞ [5, 11]
    
    two_product([100, 12, 4, 1, 2], 15) ➞ None

### Notes

  * No duplicates.
  * Sort the number.
  * Try doing this with 0(n) time complexity.
  * The list can have multiple solutions, so return the first match you find.

"""

def two_product(lst, target):
    '''
    Returns the first 2 numbers in lst whose product = target, or None if
    there isn't one.
    '''
    for i, num in enumerate(lst):
        if num and not target %num:
            other = target // num
            if other in lst[i+1:]:
                return [min(num,other), max(num,other)]

