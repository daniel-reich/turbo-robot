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
  def isPrime(n:int) -> bool:
    #returns true if input is prime number, false otherwise
    #horribly ineffective
    return not any([c for c in range(2,n) if n%c==0])
  p=[]
  mp=[]
  for i in range(2,n):
    if n%i==0 and isPrime(i):
      p.append(i)
      if n%(i*i)==0:
        #print(i)
        mp.append(i)
  return p==mp

