"""


Create a function that takes two integers and returns `true` if a digit
repeats three times in a row at any place in `num1` **AND** that same digit
repeats two times in a row in `num2`.

### Examples

    trouble(451999277, 41177722899) ➞ True
    
    trouble(1222345, 12345) ➞ False
    
    trouble(666789, 12345667) ➞ True
    
    trouble(33789, 12345337) ➞ False

### Notes

You can expect every test case to contain exactly two integers.

"""

def trouble(num1, num2):
  b = [str(num1)[i:i+3] for i in range(len(str(num1))) if len(str(num1)[i:i+3])==3]
  c = [item for item in b if all(x == item[0] for x in item)]
  if c:
    d = (c[0][0])
  else:
    return False
  e = [str(num2)[i:i+2] for i in range(len(str(num2))) if len(str(num2)[i:i+2])==2]
  f = [item for item in e if all(x == d for x in item)]
  if f:
    return True
  else:
    return False

