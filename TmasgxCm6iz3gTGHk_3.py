"""


Write a function that returns the **length of the shortest contiguous
sublist** whose sum of all elements **strictly exceeds** `n`.

### Examples

    min_length([5, 8, 2, -1, 3, 4], 9) ➞ 2
    
    min_length([3, -1, 4, -2, -7, 2], 4) ➞ 3
    # Shortest sublist whose sum exceeds 4 is: [3, -1, 4]
    
    min_length([1, 0, 0, 0, 1], 1) ➞ 5
    
    min_length([0, 1, 1, 0], 2) ➞ -1

### Notes

  * The sublist should be composed of **contiguous elements** from the original list.
  * If no such sublist exists, return `-1`.

"""

def min_length(lst, n):
  res = sorted([j-i for i in range(len(lst)) for j in range(i,len(lst)+1) if sum(lst[i:j]) > n])
  return res[0] if res else -1

