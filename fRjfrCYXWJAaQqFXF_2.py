"""


A _Primorial_ is a product of the first `n` prime numbers (e.g. `2 x 3 x 5 =
30`). `2, 3, 5, 7, 11, 13` are prime numbers. If `n` was `3`, you'd multiply
`2 x 3 x 5 = 30` or Primorial = `30`.

Create a function that returns the Primorial of a number.

### Examples

    primorial(1) ➞ 2
    
    primorial(2) ➞ 6
    
    primorial(8) ➞ 9699690

### Notes

N/A

"""

from functools import reduce
def is_prime(p):
    if p==2:
        #print ('Hey')
        return True
    for i in range(2,(p//2)+1):
        if p%i==0:
            return False
    return True
​
​
​
def primorial(n):
    i=2
    L=[]
    while n>0:
        while not is_prime(i):
            #print (is_prime(i))
            i+=1
        #i+=1
        L.append(i)
        i+=1
        n-=1
    return reduce(lambda x,y:x*y,L)

