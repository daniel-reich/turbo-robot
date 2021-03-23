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
  box = []
  i = 2
  box1 = []
  while (i*i) <= n:
    if n%i==0:
      box.append(i)
      n//=i
    else:
      i += 1
  box.append(n)
  [box1.append(i) for i in box if i not in box1]
  return box1

