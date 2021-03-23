"""


Create a function that takes a number `num` and returns each place value in
the number.

### Examples

    num_split(39) ➞ [30, 9]
    
    num_split(-434) ➞ [-400, -30, -4]
    
    num_split(100) ➞ [100, 0, 0]

### Notes

N/A

"""

def num_split(num):
  l = []
  
  if str(num)[0] == "-": 
    for i in range(1, len(str(num))): 
      l.append(int("-"+str(num)[i]+"0"*(-1-i+len(str(num)))))
  else: 
    for i in range(0, len(str(num))): 
      l.append(int(str(num)[i]+"0"*(-1-i+len(str(num)))))
  return l

