"""


Starting with either `3` or `5` and given these operations:

  * add `5`
  * multiply by `3`

You should say if it is possible to reach the target number `n`.

### Examples

    only_5_and_3(14) ➞ True
    # 14 = 3*3 + 5
    
    only_5_and_3(25) ➞ True
    # 25 = 5+5+5+5+5
    
    only_5_and_3(7) ➞ False
    # There exists no path to the target number 7

### Notes

You can solve this problem by recursion or algebra.

"""

def only_5(x):
  if x % 5 ==0:
    return True
  elif x % 5!=0:
    sisa=x%5
    for i in range (1,x):
      ni=pow(3,i)
      if ni==sisa:
        return True
      elif ni > sisa:
        return False
def only_3(x):
  lis=[]
  for i in range(1,x):
    ni=pow(3,i)
    if ni==x:
      return True
    sisa= x-ni
    if sisa%5==0:
      lis.append(i)
      break
  if len(lis)==0:
    return False  
  sis=x-pow(3,lis[0])
  if sis%5==0 and sis>0:
    return True
  
​
  return False
    
def only_5_and_3(y):
  only3=only_3(y)
  only5=only_5(y)
  if only3==True and only5==False:
    return True
  elif only3==False and only5==True:
    return True
  elif only3==False and only3==False:
    return False
  elif only3==True and only5==True:
    return True

