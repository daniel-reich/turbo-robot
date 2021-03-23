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
  
  if num>0:
    n=len(str(num))
    return [int(str(num)[i])*10**(n-i-1) for i in range(n)]
  else:
    n=len(str(num))-1
    return [(-1)*int(str(num)[1:][i])*10**(n-i-1) for i in range(n)]

