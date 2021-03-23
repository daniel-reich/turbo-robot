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
  ind = 0
  loopcount = 0
  ls = [int(i) for i in str(num)]
  while loopcount < len(ls):
    for i in ls:
      if (ind + 1) < len(ls):
        if i < ls[ind + 1]:
          x = ls.index(i)
          ls[x], ls[ind+1] = ls[ind+1], ls[x]
        ind += 1
    ind = 0
    loopcount += 1
​
  large_val = "".join(str(i) for i in ls)
  small_val = "".join(str(i) for i in list(reversed(ls)))
  return(int(large_val) - int(small_val))

