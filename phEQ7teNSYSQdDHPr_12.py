"""


You will need to write three unfinished logic gates. Continue to write the
three logic gates: AND, OR, and NOT.

### Examples

    AND(1, 1) ➞ 1
    AND(0, 0) ➞ 0
    
    OR(1, 0) ➞ 1
    OR(1, 1) ➞ 1
    
    NOT(0) ➞ 1
    NOT(1) ➞ 0

### Notes

Check the **Resources** tab for some help.

"""

def NOT(num):
  if num == 1:
    return 0
  else:
    return 1
​
def AND(num,num2):
  if num == 1 and num2 == 1:
    return 1
  else:
    return 0
​
def OR(num,num2):
  if num == 1:
    return 1
  elif num2 == 1:
    return 1
  else:
    return 0

