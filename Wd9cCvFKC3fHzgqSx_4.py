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
  n = str(abs(num))
  c = 0
  c2 = len(n)
  lst = [i for i in n]
  lst2 = []
  while len(lst2)<len(n):
    lst2.append(lst[c]+'0'*(c2-1))
    c+=1
    c2-=1
  return [-int(i) if num<0 else int(i) for i in lst2]

