"""


Write a function that takes a number and returns `True` if it's a prime;
`False` otherwise. The number can be `2^64-1` (2 to the power of 63, not XOR).
With the standard technique it would be `O(2^64-1)`, which is much too large
for the 10 second time limit imposed by Edabit.

![Sieve of
Eratosthenes](https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif)

### Examples

    prime(7) ➞ True
    
    prime(56963) ➞ True
    
    prime(5151512515524) ➞ False

### Notes

A "prime" number is a number that can only be divided by itself and `1` (upon
division the result is a whole number).

"""

def prime(x):
  for i in range(2,int(x**0.5)+1):
    if x%i==0:
      return False
  return True

