"""


Write a function that returns all the elements in an array that are **strictly
greater** than their adjacent left and right neighbors.

### Examples

    mini_peaks([4, 5, 2, 1, 4, 9, 7, 2]) ➞ [5, 9]
    # 5 has neighbours 4 and 2, both are less than 5.
    
    mini_peaks([1, 2, 1, 1, 3, 2, 5, 4, 4]) ➞ [2, 3, 5]
    
    mini_peaks([1, 2, 3, 4, 5, 6]) ➞ []

### Notes

  * Do not count boundary numbers, since they only have **one** left/right neighbor.
  * If no such numbers exist, return an empty array.

"""

def mini_peaks(lst):
  return [lst[i] for i in range(1,len(lst)-1) if lst[i]>lst[i-1] and lst[i]>lst[i+1]]

