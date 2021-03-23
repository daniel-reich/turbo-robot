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

#Finds center of mass of centrifuge, if 0,0, it's balanced
import math
from itertools import combinations
def c_fuge(n,k):
  clist=(list(combinations([i for i in range(n)],k)))
  if clist==[()]:return False
  a=0;alist=[]
  angle=2*math.pi/n
  while a<2*math.pi:
    alist.append([math.sin(a),math.cos(a)])
    a+=angle
  for i in clist:
    x=0;y=0
    for j in i:
      y+=alist[j][0]
      x+=alist[j][1]
    if abs(x/k)<.001 and abs(y/k)<.001:
      return True
  return False

