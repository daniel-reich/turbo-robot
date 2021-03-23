"""


Create a function that takes a list of numbers and returns the sum of the two
lowest **positive** numbers.

### Examples

    sum_two_smallest_nums([19, 5, 42, 2, 77]) ➞ 7
    
    sum_two_smallest_nums([10, 343445353, 3453445, 3453545353453]) ➞ 3453455
    
    sum_two_smallest_nums([2, 9, 6, -1]) ➞ 8
    
    sum_two_smallest_nums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]) ➞ 563
    
    sum_two_smallest_nums([3683, 2902, 3951, -475, 1617, -2385]) ➞ 4519

### Notes

  * Don't count negative numbers.
  * Floats and empty lists will not be used in any of the test cases.

"""

def sum_two_smallest_nums(lst):
  min1, min2 = float('+inf'), float('+inf')
  ind1 = 0
  for i in range(len(lst)):
    if lst[i] >= 0:
      if lst[i] < min1:
        min1 = lst[i]
        ind1 = i
  for i in range(len(lst)):
    if lst[i] >= 0 and i != ind1:
        if lst[i] < min2:
          min2 = lst[i]
  return min1 + min2

