"""


Create a function that takes two lists and insert the second list in the
middle of the first list.

### Examples

    tuck_in([1, 10], [2, 3, 4, 5, 6, 7, 8, 9]) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    tuck_in([15,150], [45, 75, 35]) ➞ [15, 45, 75, 35, 150]
    
    tuck_in([[1, 2], [5, 6]], [[3, 4]]) ➞ [[1, 2], [3, 4], [5, 6]]

### Notes

The first list always has two elements.

"""

def tuck_in(lst1, lst2):
    for n in range(len(lst1)):
        if n==0:
            lst2.insert(0,lst1[n])
        else:
            lst2.append(lst1[n])
    return lst2

