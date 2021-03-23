"""


Write a function to find all the prime factors of a given integer. The
function must return a list containing all the prime factors, sorted in
ascending order. Remember that _1 is neither prime nor composite_ and should
not be included in your output list.

### Examples

    prime_factorize(25) ➞ [5, 5]
    
    prime_factorize(19) ➞ [19]
    
    prime_factorize(77) ➞ [7, 11]

### Notes

  * Output list must be sorted in ascending order.
  * The only positive integer which is neither prime nor composite is 1. Return an empty list if 1 is the input.

"""

def sieve(n):
    arr = (n+1)*[True]
    arr[0] = False
    arr[1] = False
    for x in range(2,int(n**0.5)+1):
        if arr[x]:
            for y in range(2,n//x+1):
                arr[x*y] = False
    return arr
​
def pArray(n):
    ret = []
    pSieve = sieve(n)
    for x in range(2,n+1):
        if pSieve[x]:
            ret.append(x)
    return ret
​
def factors(n):
    facs = []
    for x in pArray(n):
        if x > n: break
        while n%x == 0:
            facs.append(x)
            n //= x
    if n > 1: facs.append(n)
    return facs
​
​
def prime_factorize(num):
  return factors(num)

