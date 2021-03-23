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
  if num<0:
    return [-x for x in num_split(-num)]
  
  p = 10
  ans = []
  while num:
    x = num % p
    ans.append(x)
    num-=x
    p*=10
​
  return ans[::-1]

