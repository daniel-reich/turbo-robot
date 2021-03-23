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
  #remove all bad inputs
  if num < 2:
    return []
​
  primeList = []
  i = 2
  while i < num:
  
    #figure out if i is prime
    isPrime = True
​
    for x in range(2, i):
      if i % x == 0:
        isPrime = False
    
    #if it's prime, append it to list
    if isPrime:
      primeList.append(i)
      
      
    i += 1
    
  return primeList

