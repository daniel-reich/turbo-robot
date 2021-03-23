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
    lst = []
    l = []
​
    for n in range(1,num):
        if n < 2:
            l.append(n)
        for i in range(2, n):
            if n % i == 0:
                l.append(n)
​
    for b in range(1,num):
        if b not in set(l):
            lst.append(b)
    return lst

