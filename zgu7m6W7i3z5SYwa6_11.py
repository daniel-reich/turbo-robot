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
  value1 = str(lst[0])
  value2 = str(lst[1])
  returnvalue1 = 0
  returnvalue2 = 0 
  
  for x in value1:
    returnvalue1 += int(x)
  
  for y in value2:
    returnvalue2 += int(x)
  
  if returnvalue1 == returnvalue2:
    return True 
  return False

