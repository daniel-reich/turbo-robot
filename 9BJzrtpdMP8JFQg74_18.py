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
  return [i for i in range(len(lst)) if sum(lst[:i]) == sum(lst)/2][0]

