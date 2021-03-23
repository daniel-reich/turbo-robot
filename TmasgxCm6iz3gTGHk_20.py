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

def min_length(lst, num):
  current_minimum_lst = [];
  current_minimum = 69;
  for k in range(0 , len(lst)):
    for m in range(k+1, len(lst)+1):
      if (sum(lst[k:m]) > num and m- k  < current_minimum  ):
          current_minimum_lst =  lst[k:m];
          current_minimum  = m - k;
  return len(current_minimum_lst) or  -1 ;

