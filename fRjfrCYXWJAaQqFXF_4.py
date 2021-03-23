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

def is_prime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return n!=1
​
def primorial(n):
    count=0
    i=2
    result=1
    while count<n:
        if is_prime(i):
            result*=i
            count+=1
        i+=1
    return result

