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
  sum1, sum2 = 0, 0
  while lst[0] > 0:
    sum1 += lst[0]%10
    lst[0] = int(lst[0]/10)
  while lst[1] > 0:
    sum2 += lst[1]%10
    lst[1] = int(lst[1]/10)
  return sum1 == sum2

