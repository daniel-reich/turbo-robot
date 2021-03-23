"""


Create a function that given a list, it returns the index where if split in
two-subarrays (last element of the first array has index of (foundIndex-1)),
the sum of them are equal.

### Examples

    twins([10, 20, 30, 5, 40, 50, 40, 15]) ➞ 5
    # foundIndex 5 : [10+20+30+5+40]=[50+40+15]
    
    twins([1, 2, 3, 4, 5, 5]) ➞ 4
    # [1, 2, 3, 4] [5, 5]
    
    twins([3, 3]) ➞ 1

### Notes

Return only the foundIndex, not the divided list.

"""

def twins(lst):
    s_half, s_acc = sum(lst) / 2, 0
    for i in range(len(lst)):
        s_acc += lst[i]
        if s_acc == s_half:
            return i + 1
    return 'not found'

