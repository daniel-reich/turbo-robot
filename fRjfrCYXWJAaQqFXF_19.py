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

def primorial(n):
    mul = []
    mul1 = 1
    i = 0
    while True:
        if  not is_prime(i):
            i += 1
        elif is_prime(i):
            if len(mul) == n:
                break
            mul.append(i)
            i += 1
          
    for i in mul:
        mul1 *= i         
    return mul1
def is_prime(i):
    if i >= 2:
        for k in range(2,i):
            if not i % k:
                return False
    else:
        return False
    return True

