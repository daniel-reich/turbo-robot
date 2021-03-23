"""


Given a number, return all its prime divisors in a list. Create a function
that takes a number as an argument and returns all its prime divisors.

  * n = 27
  * All divisors: `[3, 9, 27]`
  * Finally, from that list of divisors, return the prime ones: `[3]`

### Examples

    prime_divisors(27) ➞ [3]
    
    prime_divisors(99) ➞ [3, 11]
    
    prime_divisors(3457) ➞ [3457]

### Notes

N/A

"""

def is_prime(n):
  if n < 2:
    return False
  else:
    faktor = 1
    for i in range(1,n):
      if n%i == 0:
        faktor += 1
    if faktor == 2:
      return(True)
    else:
      return(False)
​
def prime_divisors(num):
  divisors = []
  prime_div = []
  for i in range(1,num+1):
    if num%i == 0:
      divisors.append(i)
  for j in divisors:
    if is_prime(j):
      prime_div.append(j)
  return(prime_div)

