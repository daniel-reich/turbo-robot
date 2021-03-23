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
  if num == 1 or num == 0:
    return []
  l = [True]*num
  l.insert(0,0)
  l[1] = False
  i = 2
  while i <= num:
    if l[i] == True:
      for j in range(i+1, num+1):
        if j%i == 0:
          l[j] = False
    i += 1
​
  p = []
  for i in range(len(l)):
    if l[i] == True:
      p.append(i)
  return p

