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
  n=str(n)
  txt=""
  j=1
  for i in n:
    txt+=n[(j*-1)]
    if j%3==0:
      txt+=","
    j+=1
  
  n=""
  j=1
  if txt[-1]==",":
    txt=txt[0:-1]
  for i in txt:
    n+=txt[(j*-1)]
    j+=1
    
  return n

