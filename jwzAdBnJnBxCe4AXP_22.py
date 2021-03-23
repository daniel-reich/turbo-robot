"""


Given a number, return the **difference** between the maximum and minimum
numbers that can be formed when the digits are rearranged.

### Examples

    rearranged_difference(972882) ➞ 760833
    # 988722 - 227889 = 760833
    
    rearranged_difference(3320707) ➞ 7709823
    # 7733200 - 23377 = 7709823
    
    rearranged_difference(90010) ➞ 90981
    # 91000 - 19 = 90981

### Notes

N/A

"""

def rearranged_difference(num):
  y=str(num)
  o=''
  p=''
  z=[]
  for i in range(len(y)):
    if y[i].isdigit():
      z.append(int(y[i]))
  z.sort()
  for i in range(len(z)):
    o+=str(z[i])
  z.reverse()
  for i in range(len(z)):
    p+=str(z[i])
  return(int(p)-int(o))

