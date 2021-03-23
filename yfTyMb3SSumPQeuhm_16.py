"""


Write a function that efficiently calculates Fibonacci terms.

### Examples

    fibonacci(1) ➞ 1
    
    fibonacci(2) ➞ 1
    
    fibonacci(4) ➞ 3
    
    fibonacci(64) ➞ 10610209857723

### Notes

The input will always be a power of two.

"""

def fibonacci(n):
    return doubling(n)[0]
​
def doubling(n):
    if n == 0:
        return(0,1)
    else:
        x,y = doubling(n//2)
        k = x*(y*2 - x)
        k1 = x**2 + y**2
        if n%2 == 0:
            return(k,k1)
        else:
            return(k1, k+k1)

