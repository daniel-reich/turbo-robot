"""


In this challenge, you have to establish if an integer is an Unprimeable
number. To be Unprimeable, when a single digit of a composite number is
exchanged with any digit from `0` up to `9`, the new number obtained **must
not be** a prime:

    number = 14
    
    Numbers obtained changing the first digit (1):
    
    04 (4), 14, 24, 34, 44, 54, 64, 74, 84, 94
    # Leading zeros are not considered
    
    Numbers obtained changing the second digit (4):
    
    10, 11, 12, 13, 14, 15, 16, 17, 18, 19
    
    # Among the two series, 11, 13, 17 and 19 are primes
    # 14 is not an unprimeable number
    
    number = 200
    
    Numbers obtained changing the first digit (2):
    
    000 (0), 100, 200, 300, 400, 500, 600, 700, 800, 900
    # Leading zeros are not considered
    
    Numbers obtained changing the second digit (0):
    
    200, 210, 220, 230, 240, 250, 260, 270, 280, 290
    
    Numbers obtained changing the third digit (0):
    
    200, 201, 202, 203, 204, 205, 206, 207, 208, 209
    
    # Among the three series, there aren't primes
    # 200 is an unprimeable number (the first of the series)

Given a non-negative integer `num`, implement a function that returns:

  * The string `"Prime Input"` if `num` is prime.
  * The string `"Unprimeable"` if `num` is Unprimeable (accordingly to the above instructions).
  * If `num` is not Unprimeable, an array containing all the primes obtained after exchanging its digits, without duplicates and sorted ascendingly.

### Examples

    is_unprimeable(200) ➞ "Unprimeable"
    
    is_unprimeable(14) ➞ [11, 13, 17, 19]
    
    is_unprimeable(2) ➞ "Prime Input"

### Notes

  * When changing the first digit, leading zeros are not considered part of the new number obtained.
  * Despite is still an unproofed theory, as far as we know every even number (except `2`) is not prime. You are free to choose to use this discriminant when you check the number obtained after the change of a digit.
  * The same concept can be applied also to primes. Primes that do not return other primes when their single digits are changed (apart from the number itself) are called _Weakly Primes_ : the first prime of this series is `294001`.

"""

def prime_factors(n):
    '''
    Returns a list of the prime factors of integer n as per above
    '''
    primes = []
    for i in range(2, int(n**0.5) + 1):
​
        while n % i == 0:
            primes.append(i)
            n //= i
​
    return primes + [n] if n > 1 else primes
​
def is_unprimeable(n):
    '''
    Returns 'Unprimeable', 'Prime Input' or a list of primes in ascending order
    for positive integer n as per the instructions above.
    '''
    if n > 1 and len(prime_factors(n)) == 1:
        return 'Prime Input'
​
    str_num = str(n)
    primes = []   # to store found primes in
​
    for i, digit in enumerate(str_num):
        for val in range(10):
            if int(digit) != val:
                num = int(str_num[:i] + str(val) + str_num[i + 1:])
                if num % 2 == 1 or num == 2:
                    if len(prime_factors(num)) == 1:
                        primes.append(num)  # prime number found
​
    return 'Unprimeable' if len(primes) == 0 else sorted(set(primes))

