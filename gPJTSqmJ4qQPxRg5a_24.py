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
  s = str(num)
  i = 0
  for c in s:
    i += int(c)
  return i - (len(s) ** 2)

