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
  lst = list(str(n))
  lst.reverse()
  l = []
  for i in range(0,len(lst)):
    if i in range(3,len(lst),3):
      l.append(lst[i]+",")
    else:
      l.append(lst[i])
  
  l.reverse()  
  return "".join(l)

