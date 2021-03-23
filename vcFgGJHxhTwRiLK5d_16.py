"""


Given a positive integer `n`, implement a function that finds the **smallest**
number that is evenly divisible by the integers `1` through `n` inclusive.

### Examples

    smallest(1) ➞ 1
    
    smallest(5) ➞ 60
    
    smallest(10) ➞ 2520
    
    smallest(20) ➞ 232792560

### Notes

N/A

"""

def smallest(n):
  if n==1:
    return 1
  lst_p=[2]
  for i in range(2,n+1):
    is_p=True
    for j in lst_p:
      if i%j==0:
        is_p=False
    if is_p:
      lst_p.append(i)
  lst_f=[]
  for i in lst_p:
    cache=i
    while cache*i<=n:
      cache*=i
    lst_f.append(cache)
  output=1
  for i in lst_f:
    output*=i
  return output

