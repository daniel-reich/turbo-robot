"""


Given a string of numbers separated by a _comma and space_ , return the
**total** of all the numbers.

### Examples

    add_nums("2, 5, 1, 8, 4") ➞ 20
    
    add_nums("1, 2, 3, 4, 5, 6, 7") ➞ 28
    
    add_nums("10") ➞ 10

### Notes

  * Numbers will always be separated by a comma and space.
  * Your function should accept negative numbers.

"""

def add_nums(nums):
  d=[]
  x=nums.split(', ')
  for i in x:
    y=int(i)
    d.append(y)
  return sum(d)

