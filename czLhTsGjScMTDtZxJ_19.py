"""


In mathematics, primorial, denoted by “#”, is a function from natural numbers
to natural numbers similar to the factorial function, but rather than
successively multiplying positive integers, the function only multiplies
**prime numbers**.

Create a function that takes an integer `n` and returns its **primorial**.

### Examples

    primorial(1) ➞ 2
    # First prime number = 2
    
    primorial(2) ➞ 6
    # Product of first two prime numbers = 2*3 = 6
    
    primorial(6) ➞ 30030

### Notes

n >= 1.

"""

def prime(n):
    a = 3
    p = [2]
    while len(p) < n:
        isPrime = True
        for i in range(2,int(a**.5)+1):
            if a%i == 0:
                isPrime = False
        if isPrime:
            p.append(a)
        a += 2
    return p
def primorial(n):
    p = prime(n)
    myans = 1
    for i in p:
        myans *= i
    return myans

