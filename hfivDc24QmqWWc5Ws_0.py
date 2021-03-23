"""


Given `num` as input, return a list with all primes up to `num` included.

![Alternative Text](https://edabit-
challenges.s3.amazonaws.com/Sieve_of_Eratosthenes_animation.gif)

### Examples

    eratosthenes(1) ➞ []
    
    eratosthenes(10) ➞ [2, 3, 5, 7]
    
    eratosthenes(20) ➞ [2, 3, 5, 7, 11, 13, 17, 19]
    
    eratosthenes(0) ➞ []

### Notes

  * Check the **Resources** tab for info on the meaning of "Eratosthenes".
  * Try solving this challenge using Eratosthenes sieve.

"""

def eratosthenes(num):
    if num < 2:
        return []
    
    sieve = [True] * num
    sieve[0], sieve[1] = False, False
​
    for i in range(2, int(num ** 0.5) + 1):
        p = i * 2
        while p < num:
            sieve[p] = False
            p += i
​
    return [i for i in range(num) if sieve[i]]

