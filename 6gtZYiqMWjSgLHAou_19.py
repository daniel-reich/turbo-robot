"""


Create a function that takes a number as an argument and returns a string
formatted to separate thousands.

### Examples

    format_num(1000) ➞ "1,000"
    
    format_num(100000) ➞ "100,000"
    
    format_num(20) ➞ "20"

### Notes

You can expect a valid number for all test cases.

"""

def format_num(n):
  n_s = str(n)
  s_l = list(n_s)
  for i in range(len(s_l)-3, 0, -3):
    s_l.insert(i, ',')
  out = ''.join(s_l)
  return out

