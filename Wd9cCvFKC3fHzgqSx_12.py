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
  i=0
  ls = []
  n = abs(num)
  while n!=0:
    mod = n%10
    pv = mod*(10**i)
    n = n//10
    if num<0:
      ls.insert(0,-pv)
    else:
      ls.insert(0,pv)
    i = i+1
  return ls

