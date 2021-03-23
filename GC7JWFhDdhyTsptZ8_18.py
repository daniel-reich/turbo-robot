"""


Sexy primes are primes that differ by 6.

For example, (5, 11) comprise a sexy prime pair, while (5, 11, 17) comprise a
set of sexy prime triplets.

Create a function that takes two numbers as argument, the set length `n` (2
for pairs, 3 for triplets), and the `limit`. Return a list of sorted tuples of
sexy primes up to (but excluding) the `limit`.

### Examples

    sexy_primes(2, 100) ➞ [(5, 11), (7, 13), (11, 17), (13, 19), (17, 23), (23, 29), (31, 37), (37, 43), (41, 47), (47, 53), (53, 59), (61, 67), (67, 73), (73, 79), (83, 89)]
    
    sexy_primes(3, 100) ➞ [(5, 11, 17), (7, 13, 19), (11, 17, 23), (17, 23, 29), (31, 37, 43), (41, 47, 53), (47, 53, 59), (61, 67, 73), (67, 73, 79)]
    
    sexy_primes(3, 250) ➞ [(5, 11, 17), (7, 13, 19), (11, 17, 23), (17, 23, 29), (31, 37, 43), (41, 47, 53), (47, 53, 59), (61, 67, 73), (67, 73, 79), (97, 103, 109), (101, 107, 113), (151, 157, 163), (167, 173, 179), (227, 233, 239)]

### Notes

N/A

"""

def sexy_primes(n, limit):
​
    aux = []
    primes = []
​
    for i in range(2, limit):
        for j in range(2, i):
            if i % j == 0:
                aux.append(i)
​
    for k in range(2, limit):
        if k not in aux:
            primes.append(k)
​
    sexy_pair = []
    sexy_triplets = []
​
    if n == 2:
        for i in range(0, len(primes)):
            for j in range(0, len(primes)):
                if primes[i] + 6 == primes[j]:
                    sexy_pair.append((primes[i], primes[j]))
        return sexy_pair
​
    if n == 3:
        for i in range(0, len(primes)):
            for j in range(0, len(primes)):
                for k in range(0, len(primes)):
                    if primes[i] + 6 == primes[j] and primes[i] + 12 == primes[k]:
                        sexy_triplets.append((primes[i], primes[j], primes[k]))
        return sexy_triplets

