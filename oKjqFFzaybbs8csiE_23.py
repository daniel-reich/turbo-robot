"""


Create a function that determines whether elements in an array can be re-
arranged to form a consecutive list of numbers where **each number appears
exactly once**.

### Examples

    cons([5, 1, 4, 3, 2]) ➞ True
    // Can be re-arranged to form [1, 2, 3, 4, 5]
    
    cons([5, 1, 4, 3, 2, 8]) ➞ False
    
    cons([5, 6, 7, 8, 9, 9]) ➞ False
    // 9 appears twice

### Notes

N/A

"""

def cons(lst):
    ideal = list(range(min(lst), max(lst) + 1))
    lst.sort()
    if lst == ideal:
        return True
    return False

