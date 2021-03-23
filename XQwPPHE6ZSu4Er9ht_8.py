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

def is_economical(n):
    def get_prime_factors(n):
        for i in range (n - 1, 1, -1):
            if (n % i):
                continue
            j = int(n / i)
            return str(get_prime_factors(i)) + ", " + str(get_prime_factors(j))
        return n
    prime_factors = get_prime_factors(n)
    if (type(prime_factors) == int):
        prime_factors = [prime_factors]
    else: 
        prime_factors = prime_factors.split(", ")
    unique_factors = [[], []]
    for factor in prime_factors:
        if (not (factor in unique_factors[0])):
            unique_factors[0].append(factor)
            unique_factors[1].append(1)
        else:
            index = unique_factors[0].index(factor)
            unique_factors[1][index] = int(unique_factors[1][index]) + 1
    answer = 0
    for factor in unique_factors[0]:
        answer += len(str(factor))
    for expo in unique_factors[1]:
        if (int(expo) > 1):
            answer += len(str(expo))
    if (answer < len(str(n))):
        return "Frugal"
    if (answer > len(str(n))):
        return "Wasteful"
    return "Equidigital"

