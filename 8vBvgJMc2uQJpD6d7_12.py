"""


Create a function that returns a list containing the prime factors of whatever
integer is passed to it.

### Examples

    prime_factors(20) ➞ [2, 2, 5]
    
    prime_factors(100) ➞ [2, 2, 5, 5]
    
    prime_factors(8912234) ➞ [2, 47, 94811]

### Notes

  * Implement your solution using trial division.
  * Your solution should not require recursion.

"""

import math
​
def is_prime_fast(number):
    sqrt_number = math.ceil(math.sqrt(number))
    if number <= 1:
        return False
    if number == 2:
        return True
    if(number%2==0):
        return False    
    for factor in range(2, sqrt_number + 1):
        if number % factor == 0:
            return False
    return True
​
def prime_factors(n):
    prime_list = []
    i = 2
    while n != 1:
        if is_prime_fast(i):
            if n % i == 0:
                n = n / i
                prime_list.append(i)
            else:
                i += 1
        else:
            i += 1
    return prime_list

