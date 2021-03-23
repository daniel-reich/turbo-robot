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

def prime_divisors(n):
  
  
  l = []
  while n%2==0:
    n//=2
    l.append(2)
  for i in range(3,int(n**.5)+1,2):
    while n%i==0:
      n//=i
      l.append(i)
  if n>=2:
    l.append(n)
  return sorted(list(set(l)))

