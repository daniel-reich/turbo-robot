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
  num1=str(lst[0])
  num2=str(lst[1])
  total1=0
  total2=0
  for i in num1:
    total1+=int(i)
  for i in num2:
    total2+=int(i)
  return total1==total2

