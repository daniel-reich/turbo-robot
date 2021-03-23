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
  return abs(num - 1)
​
def AND(num1,num2):
  return num1 + num2 == 2
​
def OR(num1,num2):
  return num1 + num2 > 0

