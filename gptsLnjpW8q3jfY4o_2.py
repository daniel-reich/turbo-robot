"""


Create a function that takes a integer number `n` and returns the formula for
`(a+b)^n` as a string.

### Examples

    Formula(0) ➞ "1"
    
    Formula(1) ➞ "a+b"
    
    Formula(2) ➞ "a^2+2ab+b^2"
    
    Formula(-2) ➞ "1/(a^2+2ab+b^2)"
    
    Formula(3) ➞ "a^3+3a^2b+3ab^2+b^3"
    
    Formula(5) ➞ "a^5+5a^4b+10a^3b^2+10a^2b^3+5ab^4+b^5"

### Notes

Don't put the following in your string:

  * `spaces`
  * `*`
  * `^1`
  * `a^0`
  * `b^0`

"""

import re
def Formula(n):
  if n<0: return "1/({})".format(Formula(-n))
  if n==0: return '1'
  pre = '+'.join([str(comb(n,k))+'a^'+str(n-k)+'b^'+str(k) for k in range(0,n+1)])
  prepre = re.sub(r'a\^0|b\^0|\^1(?!\d)','',pre)
  return re.sub(r"(?<!\d)(?<!\^)1(?!\d)",'',prepre)
​
def comb(n,k):
  ans = 1
  for i in range(k): 
    ans = ans*(n-i)//(i+1)
  return ans

