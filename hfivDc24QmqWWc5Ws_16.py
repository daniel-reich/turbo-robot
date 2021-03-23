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

def prime(n):
  a=[]
  for i in range(1,n+1):
    if n%i==0:
      a.append(i)
  return len(a)==2
def eratosthenes(num):
  x=[]
  for i in range(2,num+1):
    if prime(i):
      x.append(i)
  return x

