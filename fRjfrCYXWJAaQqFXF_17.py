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
    primes = []
    counter = 2
    while len(primes) < n:
        if counter == 2:
              primes.append(counter)
        elif all(counter % i for i in range(2, counter)) == True:
            primes.append(counter)
        counter += 1
    result = 1
    for i in primes:
        result *= i
    return result

