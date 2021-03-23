"""


Create a function that can nest a flat list to represent an incremental depth
level sequence.

### Examples

    incremental_depth([1, 2]) ➞ [1, [2]]
    
    incremental_depth([1, 2, 3, 4, 5]) ➞ [1, [2, [3, [4, [5]]]]]
    
    incremental_depth([1, 3, 2, 6]) ➞ [1, [3, [2, [6]]]]
    
    incremental_depth(["dog", "cat", "cow"]) ➞ ["dog", ["cat", ["cow"]]]

### Notes

  * The elements do not matter to the function, you should increment by index.
  * Expect the array length to be from 2-20.

"""

def incremental_depth(lst):
    lst1 = [lst[-1]]
    for i in range(2, len(lst)+1):
        lst1 = [lst[-1*i]]+[lst1]
    return lst1

