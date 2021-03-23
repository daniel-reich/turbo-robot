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
  return not num
​
def AND(num,num2):
  return num and num2 == 1
​
def OR(num,num2):
  return num == 1 or num2 == 1

