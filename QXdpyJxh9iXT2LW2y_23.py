"""


In mathematics, a semiprime is a natural number that is the product of two
prime numbers. The two primes in the product may equal each other, so the
semiprimes include the squares of prime numbers.

Create a function that takes a number `n` as an argument and returns two
lists, one list with all the semiprimes < `n` and the other with all the
semiprimes < `n` and that are not square numbers.

### Examples

    semiprimes(20) ➞ ([4, 6, 9, 10, 14, 15], [6, 10, 14, 15])
    
    semiprimes(157) ➞ ([4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95, 106, 111, 115, 118, 119, 121, 122, 123, 129, 133, 134, 141, 142, 143, 145, 146, 155], [6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95, 106, 111, 115, 118, 119, 122, 123, 129, 133, 134, 141, 142, 143, 145, 146, 155])
    
    semiprimes(1), ([], [])

### Notes

N/A

"""

def semiprimes(n):
    all_semiprimes = [i for i in range(4,n) if check_semi(i)]
    not_squares = [i for i in all_semiprimes if i**0.5%1]
    return all_semiprimes, not_squares
​
def check_semi(n, i=2):
    factors = []
    while i <= n:
        while not n%i:
            factors.append(i)
            n //= i
        i += 1
    return True if len(set(factors)) <= 2 and len(factors) == 2 else False
