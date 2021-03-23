"""


Create a function that takes a list of positive and negative numbers. Return a
list where the first element is the **count** of positive numbers and the
second element is the **sum** of negative numbers.

### Examples

    sum_neg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) ➞ [10, -65]
    # There are a total of 10 positive numbers.
    # The sum of all negative numbers equals -65.
    
    sum_neg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34]) ➞ [7, -252]
    
    sum_neg([91, -4, 80, -73, -28]) ➞ [2, -105]
    
    sum_neg([]) ➞ []

### Notes

  * If given an empty list, return an empty list: `[]`
  * 0 is not positive.

"""

def sum_neg(lst):
  l = []
  if len(lst)== 0:
    return l
  count = 0
  sum1 = 0
  for x in lst:
    if x > 0:
      count += 1
    else:
      sum1 += x
  l.append(count)
  l.append(sum1)
  return l

