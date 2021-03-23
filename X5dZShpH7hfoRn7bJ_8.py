"""


A centrifuge, as you probably know, is a laboratory device used to separate
fluids based on density. The separation is achieved through centripetal force
by spinning a collection of test tubes at high speeds. This means, the
configuration needs to be in balance.

Create a function that takes two numbers as arguments `n` and `k` and returns
`True` if the configuration is balanced and `False` if it's not. To check out
the formula, look at the **resources tab**.

![The Centrifuge Problem with 6 Holes, n=6](https://edabit-
challenges.s3.amazonaws.com/6_hole_centrifuge.png)

Here are the valid configurations for _n_ = 6, _k_ = 2, 3, 4 and 6.

### Examples

    c_fuge(6, 4) ➞ True
    
    c_fuge(2, 1) ➞ False
    
    c_fuge(3, 3) ➞ True

### Notes

  * One test tube `k = 1` is **never** in balance.
  * One hole `n = 1` is **never** in balance, even empty.

"""

def c_fuge(n, k):
  def f(sum,lst):
    if sum in lst:
      return True
    elif sum<=0:
      return False
    else:
      ans=False
      for i in range(len(lst)):
        if f(sum-lst[i],lst)==True:
          ans=True
          break
      return ans
  def lst_prime(x):
    if x==1:
      return []
    elif x==2:
      return [2]
    else:
      first=x
      for i in range(2,int(x**0.5)+1):
        if x%i==0:
          first=i
          break
      return [first]+lst_prime(int(x/first))
  if n==1 or k==1:
    return False
  elif n==k:
    return True
  else:
    if f(k,lst_prime(n))==True and f(n-k,lst_prime(n))==True:
      return True
    else:
      return False

