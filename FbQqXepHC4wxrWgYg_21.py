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

def prime_divisors(num):
  if num == 1 or num == 0:
    return num
  div = []
  p_div = []
  t = 0
  for _ in range(2,num+1):
    if num % _ == 0:
      div.append(_)
  for var in div:
    for res in range(2,var+1):
      if var % res == 0:
        t = t + 1
    if t == 1:
      p_div.append(var)
      t = 0
    else:
      t = 0
  return p_div

