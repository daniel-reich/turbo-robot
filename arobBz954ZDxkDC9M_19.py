"""


Given an integer, create a function that returns the next prime. If the number
is prime, return the number itself.

### Examples

    next_prime(12) ➞ 13
    
    next_prime(24) ➞ 29
    
    next_prime(11) ➞ 11
    # 11 is a prime, so we return the number itself.

### Notes

N/A

"""

def check_prime(num):
    is_prime = False
    
    factors = []
    
    num_of_factors = 0
    
    i = 1
    while i <= num:
        if num % i == 0:
            factors.append(i)
            num_of_factors += 1
        i += 1
​
    if num_of_factors == 2:
        is_prime = True
        return is_prime
    else:
        return is_prime
​
def next_prime(num):
    next_prime_num = 0
    
    if num < 2:
        return "Invalid input. Please enter an integer greater than 1."
    
    check_prime_num = check_prime(num)
    
    if check_prime_num == True:
        next_prime_num = num
        return next_prime_num
    
    j = num + 1
    while next_prime_num == 0:
        possible_next_prime = check_prime(j)
        
        if possible_next_prime == True:
            next_prime_num = j
            return next_prime_num
        
        j += 1

