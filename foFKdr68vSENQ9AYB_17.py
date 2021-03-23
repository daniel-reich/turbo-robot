"""


Create a function that takes a list and returns the sum of all numbers in the
list.

### Examples

    get_sum_of_elements([2, 7, 4]) ➞ 13
    
    get_sum_of_elements([45, 3, 0]) ➞ 48
    
    get_sum_of_elements([-2, 84, 23]) ➞ 105

### Notes

N/A

"""

def get_sum_of_elements(lst):
  sum = 0
  for element in lst:
    sum += element
  return sum

