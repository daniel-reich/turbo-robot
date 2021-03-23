"""


Create a function that takes two integers, `num` and `n`, and returns an
integer which is divisible by `n` and is the closest to `num`. If there are
two numbers equidistant from `num` and divisible by `n`, select the larger
one.

### Examples

    round_number(33, 25) ➞ 25
    
    round_number(46, 7) ➞ 49
    
    round_number(133, 14) ➞ 140

### Notes

`n` will always be a positive number.

"""

def round_number(num, n):
  a=[(num//n-1)*n, (num//n)*n, (num//n+1)*n]
  b=[abs((num//n-1)*n-num),abs((num//n)*n-num),abs((num//n+1)*n-num)]
  dct={b[i] : a[i] for i in range(len(a))}
  return dct[min(dct.keys())]

