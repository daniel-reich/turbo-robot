"""


Create a function that takes a list of numbers and returns a list where each
number is the sum of itself + all previous numbers in the list.

### Examples

    cumulative_sum([1, 2, 3]) ➞ [1, 3, 6]
    
    cumulative_sum([1, -2, 3]) ➞ [1, -1, 2]
    
    cumulative_sum([3, 3, -2, 408, 3, 3]) ➞ [3, 6, 4, 412, 415, 418]

### Notes

Return an empty list if the input is an empty list.

"""

def cumulative_sum(lst):
  additive_list = [0]
  for n in range(len(lst)):
    additive_list.append(lst[n]+additive_list[n])
  additive_list.remove(0)
  return additive_list

