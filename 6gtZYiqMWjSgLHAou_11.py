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
  ns = str(n)
  for i in [3, 7, 11]:
    if len(ns) > i:
      ns = ns[:-i]+','+ns[-i:]
  return ns

