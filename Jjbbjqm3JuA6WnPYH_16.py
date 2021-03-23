"""


Python offers some bit operations but not bit rotation. To complete that,
create a function that takes three parameters:

  1. `n`: Integer, which in binary representaion should be rotated.
  2. `m`: Number of rotation steps that should be performed.
  3. `d`: Boolean value; `True` = rotation right, `False` = rotation left.

Your function should return an integer as a result of its rotated binary
representation.

### Examples

    bit_rotate(8, 1, True) ➞ 4
    # 8 in bin: 1000, rotated 1 step to the right: 0100, in dec: 4
    
    bit_rotate(16, 1, False) ➞ 1
    # 16 in bin: 10000, rotated 1 step to the left: 00001, in dec: 1
    
    bit_rotate(17, 2, False) ➞ 6
    # 17 in bin: 10001, rotated 2 steps to the left: 00110, in dec: 6

### Notes

  * For parameters use unsigned integers only.
  * There is a solution with string operations and combined bit operations.

"""

def bit_rotate(n, m, d):
  bin = format(n,"b")
  one = []
  for i in range(len(bin)):
    if bin[i]=='1':
      one.append(i)
  
  if d==True:
    for i in range(len(one)):
      if one[i]+m > (len(bin)-1):
        tmp = (m-(len(bin)-1-one[i]))%len(bin)
        if tmp == 0:
          one[i] = len(bin)-1
        else:
          one[i] = tmp-1
      else :
        one[i] = one[i]+m
  else:
    for i in range(len(one)):
      if one[i]-m < 0:
        tmp = (m-one[i])%len(bin)
        if tmp == 0:
          one[i] = 0
        else:
          one[i] = len(bin)-tmp
      else :
        one[i] = one[i]-m
​
  sum = 0
  for i in range(len(bin)):
    for j in one:
      if i == len(bin)-j-1:
        sum += 2**i
  return sum

