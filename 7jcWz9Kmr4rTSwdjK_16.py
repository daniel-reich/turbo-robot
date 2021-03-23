"""


Write a function to find all the prime factors of a given integer. The
function must return a list containing all the prime factors, sorted in
ascending order. Remember that _1 is neither prime nor composite_ and should
not be included in your output list.

### Examples

    prime_factorize(25) ➞ [5, 5]
    
    prime_factorize(19) ➞ [19]
    
    prime_factorize(77) ➞ [7, 11]

### Notes

  * Output list must be sorted in ascending order.
  * The only positive integer which is neither prime nor composite is 1. Return an empty list if 1 is the input.

"""

def prime_factorize(num):
    factors = []
    divisor = 2
    while divisor <= num:
        if not is_prime(divisor):
            divisor += 1
        elif num % divisor == 0:
            factors.append(divisor)
            num = num / divisor
        else:
            divisor += 1
    return factors
​
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    if len(factors(num)) == 2:
        return True
    else:
        return False
​
def factors(num):
    factors = set()
    limit = int(num ** 0.5) + 1
    for i in range(1, limit):
        if num % i == 0:
            factors.add(i)
            factors.add(num / i)
    return factors

