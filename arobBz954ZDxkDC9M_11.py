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

def next_prime(num):
  lst = [ ]  
  for n in range(1,200):
    for i in range(2,n//2+1):
      if n%i == 0:break
    else: lst.append(n)
  for i in lst:
    if num in lst: return num
    if i >num:return i

