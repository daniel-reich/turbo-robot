"""


Given a list of numbers, create a function which returns the list but with
**each element's index in the list added to itself**. This means you add _0 to
the number at index 0, add 1 to the number at index 1, etc..._

###  Examples

    add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
    
    add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
    
    add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

### Notes

You'll only get numbers in the list.

"""

add_indexes=lambda l:[a+i for i,a in enumerate(l)]

