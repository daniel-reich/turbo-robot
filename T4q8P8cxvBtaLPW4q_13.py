"""


Create a function that takes an integer argument and returns a list of prime
numbers found in the decimal representation of that number (not factors).

For example, `extract_primes(1717)` returns `[7, 7, 17, 17, 71]`.

The list should be in acending order. If a prime number appears more than
once, every occurance should be listed. If no prime numbers are found, return
an empty list.

### Examples

    extract_primes(1) ➞ []
    
    extract_primes(7) ➞ [7]
    
    extract_primes(73) ➞ [3, 7, 73]
    
    extract_primes(103) ➞ [3]
    
    extract_primes(1313) ➞ [3, 3, 13, 13, 31, 131, 313]

### Notes

  * All test cases are positive real integers.
  * Some numbers will have leading zeros. For example, the number `103` contains the prime number `3`, but also contains `03`. These should be treated as the same number, so the result would simply be `[3]`.

"""

from math import sqrt
​
def extract_primes(num):
    digits=[i for i in str(num)]
    primes=[]
​
    set_size=1
​
    while set_size<=len(digits):
        for i in range(len(digits)):
            if i+set_size> len(digits):
                continue
​
            test= "".join(digits[i:i+set_size])
​
            if str(int(test))!= test:
                continue
​
​
            if isPrime(int(test)):
                primes.append(int(test))
        set_size+=1
​
    primes.sort()
    return primes
​
def isPrime(num):
    if num<= 1:
        return False
​
    for n in range (2,int(sqrt(num))+1):
        if num % n==0:
            return False
    return True

