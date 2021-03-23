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

from itertools import combinations_with_replacement
def prime_set (n):
  prime=[]
  for i in range (2,n+1):
    counter=0
    for j in range (1,i+1):
      if i%j ==0:
        counter+=1
    if counter <=2:
      prime.append(i)
  return prime
​
def c_fuge(n, k):
  if k==1 or k==0:
    return False
  if k==n:
    return True
  lst1,all_,sumsum=prime_set(n),[],[]
  lst = [i for i in lst1 if n%i==0]
  if n in lst:
    return False
  for j in range (1,n//2):
    all_.append(list(combinations_with_replacement(lst,j)))
  
  sumsum=[sum(j) for i in all_ for j in i]
  if k in sumsum and (n-k) in sumsum:
    return True
  return False

