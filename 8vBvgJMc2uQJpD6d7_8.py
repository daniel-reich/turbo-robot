"""


Create a function that returns a list containing the prime factors of whatever
integer is passed to it.

### Examples

    prime_factors(20) ➞ [2, 2, 5]
    
    prime_factors(100) ➞ [2, 2, 5, 5]
    
    prime_factors(8912234) ➞ [2, 47, 94811]

### Notes

  * Implement your solution using trial division.
  * Your solution should not require recursion.

"""

def prime_factors(num):
  num = int(num)
  lst = []
  while int(num)%2 == 0:
    lst.append(2)
    num = num/2
  for i in range(3, int(num*num)):
    if num == 1:
      break
    while num%i == 0:
      lst.append(i)
      num = num/i
  return lst

