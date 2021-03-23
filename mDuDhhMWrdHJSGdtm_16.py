"""


You are given a number `n`. Determine whether `n` has exactly **3 divisors**
or not.

### Examples

    is_exactly_three(4) ➞ True
    # 4 has only 3 divisors: 1, 2 and 4
    
    is_exactly_three(12) ➞ False
    # 12 has 6 divisors: 1, 2, 3, 4, 6, 12
    
    is_exactly_three(25) ➞ True
    # 25 has only 3 divisors: 1, 5, 25

### Notes

1 ≤ n ≤ 10^12

"""

def prima(x):
  for i in range (2,x+1):
    if x%i==0 and x !=i:
      return False
    elif x % i==0 and x==i:
      return True
def is_exactly_three(n):
  if n==1:
    return False
  elif n!=1:
    ni=pow(n,1/2)
    a=list(str(ni))
    b=a.index(".")
    c=a[b:]
    if len(c)==2:
      chekprima=prima(int(ni))
      if chekprima==True:
        return True
      elif chekprima==False:
        return False
    elif len(c)!=2:
      return False

