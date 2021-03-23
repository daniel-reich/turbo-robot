"""


Create a function that returns `True` if a given inequality expression is
correct and `False` otherwise.

### Examples

    correct_signs("3 < 7 < 11") ➞ True
    
    correct_signs("13 > 44 > 33 > 1") ➞ False
    
    correct_signs("1 < 2 < 6 < 9 > 3") ➞ True

### Notes

N/A

"""

import operator, re
def correct_signs(txt):
  ops = {'<': operator.lt, '>': operator.gt}
  opsRegex = re.compile(r'<|>')
  opsList = opsRegex.findall(txt)
  numList = [int(i) for i in re.split(' < | > ', txt)]
  
  for i in range(len(opsList)):
    if not ops[opsList[i]](numList[i], numList[i + 1]):
      return False
  return True

