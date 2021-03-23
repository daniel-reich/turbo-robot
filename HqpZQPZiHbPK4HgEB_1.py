"""


Maxie is the largest number that can be obtained by **swapping two digits** ,
Minnie is the smallest. Write a function that takes a number and returns Maxie
and Minnie. Leading zeros are not permitted.

### Examples

    maxmin(12340) ➞ (42310, 10342)
    
    maxmin(98761) ➞ (98761, 18769)
    
    maxmin(9000) ➞ (9000, 9000)
    # Sometimes no swap needed.
    
    maxmin(11321) ➞ (31121, 11123)

### Notes

N/A

"""

def maxmin(n):
  def f(n,l):
    for i,x in enumerate(l):
      if x!=n[i]:p=i+n[i:].rfind(x);return int(n[:i]+n[p]+n[i+1:p]+n[i]+n[p+1:])
    return int(n)
  n=str(n)
  return f(n,sorted(n,reverse=1)),f(n,[min(n,key=lambda y:(y,'z')[y=='0'])]+sorted(n[1:]))

