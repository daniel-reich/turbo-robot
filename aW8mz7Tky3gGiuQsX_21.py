"""


Given a positive number x:

    p = (p1, p2, …)
    # Set of *prime* factors of x

If the square of every item in p is also a factor of x, then x is said to be a
**_powerful_** number.

Create a function that takes a number and returns `True` if it's powerful,
`False` if it's not.

### Examples

    is_powerful(36) ➞ True
    # p = (2, 3) (prime factors of 36)
    # 2^2 = 4 (factor of 36)
    # 3^2 = 9 (factor of 36)
    
    is_powerful(27) ➞ True
    
    is_powerful(674) ➞ False

### Notes

N/A

"""

def is_powerful(n):
  nb = n
  p=[]
  for i in range(2,n):
    if nb%i == 0 :
      p.append(i)
      while nb%i == 0 :
        nb = nb/i
  powerful = True
  for div in p:
    if powerful : 
      powerful =(n%(div**2) == 0)
  return powerful

