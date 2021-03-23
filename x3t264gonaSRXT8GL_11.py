"""


Given an integer `n`, create a function that returns the length of the
repeating cycle of the sequence **1/n**. If the cycle is non-repetitive,
return `-1`.

    repeating_cycle(13) ➞ 6
    # 1/13 = 0.076923 076923 076923 076923 ...
    # length of `076923` is 6.

### Examples

    repeating_cycle(5) ➞ -1
    # 1/5 = 0.2 (non-repeative)
    
    repeating_cycle(33) ➞ 2
    # 1/33 = 0.03 03 03 03 03 03 03 03
    # length of `03` is 2
    
    repeating_cycle(197) ➞ 98

### Notes

Return `-1` if the repeating cycle does not start from the first decimal
place. As an example, 1/22 = 0.0 45 45 45 45, your function should return `-1`
in this case.

"""

def repeating_cycle(n):
  rest=0
  value=1
  out=[]
​
  for i in range(50000):
    value*= 10
    r=value//n
    value-=r*n
    tmp=[r,value]
    #print(tmp, tmp in out)
    if i>0 and tmp  == out[0]:
      print(out,tmp)
      return ( len(out) -  out.index(tmp) )
    out.append(tmp)
  return -1

