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

def func(num):
  count=0
  for i in str(num):
    count+=(int(i)-len(str(num)))
  return count

