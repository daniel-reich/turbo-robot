"""


Write a function that takes a list of numbers and returns a list with two
elements:

  1. The first element should be the sum of all **even** numbers in the list.
  2. The second element should be the sum of all **odd** numbers in the list.

### Example

    sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
    # 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9
    
    sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])
    
    sum_odd_and_even([0, 0]) ➞ [0, 0])

### Notes

Count `0` as an **even** number.

"""

def sum_odd_and_even(lst):
  lst1 = [0, 0]
  t1 = 0
  t2 = 0
  for i in lst:
    if (i % 2) == 0:
      t1+=i
    else:
      t2+=i
  lst1 = [t1, t2]
  print(lst1)
  return lst1

