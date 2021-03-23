"""


A number is Economical if the quantity of digits of its prime factorization
(including exponents greater than 1) is equal to or lower than the digit
quantity of the number itself.

Given an integer `n`, implement a function that returns a string:

  * `"Equidigital"` if the quantity of digits of the prime factorization (including exponents greater than 1) is equal to the quantity of digits of `n`;
  * `"Frugal"` if the quantity of digits of the prime factorization (including exponents greater than 1) is lower than the quantity of digits of `n`;
  * `"Wasteful"` if none of the two above conditions is true.

### Examples

    is_economical(14) ➞ "Equidigital"
    # The prime factorization of 14 (2 digits) is [2, 7] (2 digits)
    # Exponents equal to 1 are not counted
    
    is_economical(125) ➞ "Frugal"
    # The prime factorization of 125 (3 digits) is [5^3] (2 digits)
    # Notice how exponents greater than 1 are counted
    
    is_economical(1024) ➞ "Frugal"
    # The prime factorization of 1024 (4 digits) is [2^10] (3 digits)
    
    is_economical(30) ➞ "Wasteful"
    # The prime factorization of 30 (2 digits) is [2, 3, 5] (3 digits)

### Notes

  * Any given `n` will be a positive integer greater than 1.
  * Remember to count also the exponents greater than 1 into the prime factorization: 2¹ = 2 (one digit), 2² = 22 (two digits), 2¹° = 210 (three digits)...

"""

from collections import defaultdict
​
​
def is_economical(n):
    def is_prime(n):
        if n > 1:
            # check for factors
            for i in range(2, n):
                if (n % i) == 0:
                    return False
            return True
        else:
            return False
​
    n_length = len(str(n))
    total = defaultdict(int)
    score = 0
    while True:
        for i in range(2, n+1):
            if is_prime(i) and n % i == 0:
                n = n // i
                total[i] += 1
                if is_prime(n) or n == 1:
                    if n > 1:
                        total[n] += 1
                    for k, v in total.items():
                        if v > 1:
                            score += len(str(k)) + len(str(v))
                        else:
                            score += len(str(k))
                    if score == n_length:
                        return 'Equidigital'
                    if score < n_length:
                        return 'Frugal'
                    return 'Wasteful'
                break

