"""


Given two arguments, return a list which contains these two arguments.

### Examples

    make_pair(1, 2) ➞ [1, 2]
    
    make_pair(51, 21) ➞ [51, 21]
    
    make_pair(512124, 215) ➞ [512124, 215]

### Notes

N/A

"""

def make_pair(num1, num2):
  list = [num1]
  list.append(num2)
  return list

