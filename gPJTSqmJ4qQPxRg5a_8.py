"""


By looking at the inputs and outputs below, try to figure out the pattern and
write a function to execute it for any number.

### Examples

    func(3456) ➞ 2
    
    func(89265) ➞ 5
    
    func(97) ➞ 12
    
    func(2113) ➞ -9

### Notes

N/A

"""

import math
def func(num):
  x = num
  count = 1
  list = []
  sum = 0
  while x>10:
    list.append(x%10)
    count+=1
    x=math.floor(x/10)
  list.append(x%10)
  for i in range(len(list)):
    sum+=(list[i]-count)
  return sum

