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
  sum_even=0
  sum_odd=0
  result=[]
  for i in lst:
    if i%2==0:
      sum_even=sum_even+i
    else:
      sum_odd=sum_odd+i
  result.append(sum_even)
  result.append(sum_odd)
  return result

