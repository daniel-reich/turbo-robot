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

def prime_factors(n):
    primes = []   
    
    while n % 2 == 0: #while n is even
        primes += 2, #add 2 to list
        n = n / 2 #divide by 2
    
    for i in range(3, int(n**0.5) + 1, 2): 
        while n % i== 0: 
            primes += int(i), 
            n = n / i 
    
    if n > 2: 
        primes += int(n),
        
    return primes

