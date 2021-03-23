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

def sum(str):
  sum=0
  for i in str:
    sum+=int(i)
  return sum
  
def is_equal(lst):
  if(len(lst)==2):
    return sum(str(lst[0]))==sum(str(lst[1]))

