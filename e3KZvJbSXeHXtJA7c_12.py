"""


Create a function that returns the sum of missing numbers.

### Examples

    sum_missing_numbers([1, 3, 5, 7, 10]) ➞ 29
    # 2 + 4 + 6 + 8 + 9
    
    sum_missing_numbers([10, 7, 5, 3, 1]) ➞ 29
    
    sum_missing_numbers([10, 20, 30, 40, 50, 60]) ➞ 1575

### Notes

The minimum and maximum value of the given list are the inclusive bounds of
the numeric range to consider when searching for missing numbers.

"""

def sum_missing_numbers(lst):
  lst.sort()
  sumList = 0
  for el in lst:
    sumList += el
  expectedSumHigh = lst[len(lst)-1]*(lst[len(lst)-1] + 1)/2
  expectedSumLow = 0
  if lst[0] != 1:
    expectedSumLow = (lst[0] - 1)*(lst[0])/2
  return expectedSumHigh - expectedSumLow - sumList

