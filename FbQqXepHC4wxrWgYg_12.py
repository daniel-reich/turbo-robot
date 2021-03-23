"""


Given a number, return all its prime divisors in a list. Create a function
that takes a number as an argument and returns all its prime divisors.

  * n = 27
  * All divisors: `[3, 9, 27]`
  * Finally, from that list of divisors, return the prime ones: `[3]`

### Examples

    prime_divisors(27) ➞ [3]
    
    prime_divisors(99) ➞ [3, 11]
    
    prime_divisors(3457) ➞ [3457]

### Notes

N/A

"""

def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def prime_divisors(n):
    x=[]
    i=2
    while i<=n:
        if n%i==0:
            if isprime(i):
                x.append(i)
        i=i+1
    return x

