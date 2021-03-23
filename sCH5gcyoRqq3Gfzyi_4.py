"""


Create a function which validates whether a given number exists, and could
represent a real life quantity. Inputs will be given as a string.

### Examples

    valid_str_number("3.2") ➞ True
    
    valid_str_number("324") ➞ True
    
    valid_str_number("54..4") ➞ False
    
    valid_str_number("number") ➞ False

### Notes

Accept numbers such as `.5` and `0003`.

"""

def is_numeric(c):
  if ord(c)>=ord('0') and ord(c)<=ord('9'):
    return True
  return False
  #32..2
  #.3
  #21.22
  #fas223
  #((()))
  #??f322
  #2334.33?
  
def valid_str_number(n):
  c_count=0
  for x in n:
    if x=='.':
      if c_count==0:
        c_count = 1
      else:
        return False
    elif not is_numeric(x):
      return False
  return True

