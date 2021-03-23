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

def prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def is_powerful(num):
    d=[]
    r=[]
    s=[]
    for i in range(2,num+1):
        if prime(i):
            d.append(i)
    for j in d:
        if num%j==0:
            s.append(j)
            
    for i in d:
        t=i**2
        if num%t==0:
            r.append(t)
          
    if len(r)==len(s):
        return True
    else:
        return False

