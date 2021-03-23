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
  new_lst = list(map(lambda n: sum([int(x) for x in str(n)]), lst))
  return new_lst[0] == new_lst[1]

