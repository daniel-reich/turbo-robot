"""


Create a function that takes a list of numbers between 1 and 10 (excluding one
number) and returns the missing number.

### Examples

    missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
    
    missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
    
    missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7

### Notes

  * The list of numbers will be **unsorted** (not in order).
  * Only one number will be missing.

"""

def missing_num(lst):
    check = 1
    for num in lst:
        if check not in lst:
            continue
        check+=1
    return check

