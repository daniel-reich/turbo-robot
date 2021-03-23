"""


Create a function that returns an array that expands by 1 from 1 to the value
of the input, and then reduces back to 1. Items in the lists will be the same
as the length of the lists.

### Examples

    diamond_arrays(1) ➞ [[1]]
    
    diamond_arrays(2) ➞ [[1], [2, 2], [1]]
    
    diamond_arrays(5) ➞ [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5], [4, 4, 4, 4], [3, 3, 3], [2, 2], [1]]

### Notes

N/A

"""

def diamond_arrays(x):
    lst = []
    for a in range(1,x+1):
        lst.append(a * list(str(a)))
        for z in lst:
            for i,y in enumerate(z):
                z[i] = int(y)
    return lst[:-1] + lst[::-1]

