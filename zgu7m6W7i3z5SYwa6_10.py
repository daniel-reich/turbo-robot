"""


Write a function that takes a list of two numbers and determines if the sum of
the **digits** in each number are equal to each other.

### Examples

    is_equal([105, 42]) ➞ True
    # 1 + 0 + 5 = 6
    # 4 + 2 = 6
    
    is_equal([21, 35]) ➞ False
    
    is_equal([0, 0]) ➞ True

### Notes

N/A

"""

def is_equal(lst):
  lst1 = [i for i in str(lst[0])]
  lst2 = [i for i in str(lst[1])]
  sum1=0
  sum2=0
  for i in lst1:
    sum1 = sum1+int(i)
  for i in lst2:
    sum2 = sum2+int(i)
  if sum1==sum2:
    return True
  else:
    return False

