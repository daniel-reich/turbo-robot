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
  if num>=0:
    count=len(str(num))-1
    lst=[]
    for i in str(num):
      lst.append(int(i)*(10**count))
      count=count-1
  if num<0:
    num=num*(-1)
    count=len(str(num))-1
    lst=[]
    for i in str(num):
      lst.append((-1)*int(i)*(10**count))
      count=count-1
  return lst

