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

def eratosthenes(n):
    res = [0,0] + [1]*(n-2)
    for i in range(2, int(n**0.5)+1):
        res[i*i::i] = [0] * ((n-1)//i - i + 1)
    return [i for i,v in enumerate(res) if v]

