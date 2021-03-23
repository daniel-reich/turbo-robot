"""


Create a function that takes a multidimensional list and returns the total
count of numbers in that list.

### Examples

    count_number([["", 17.2, 5, "edabit"]]) ➞ 2
    # 17.2 and 5.
    
    count_number([[[[[2, 14]]], 2, 3, 4]]) ➞ 5
    # 2, 14, 2, 3 and 4.
    
    count_number([["number"]]) ➞ 0

### Notes

Input may be a list of numbers, strings and empty lists.

"""

def count_number(lst, c=0):
    if not lst:
        return c
    
    if type(lst[0])!=list:
        if type(lst[0])!=str:
            c+=1
        return count_number(lst[1:], c)
    
    return count_number(lst[0]+lst[1:], c)

