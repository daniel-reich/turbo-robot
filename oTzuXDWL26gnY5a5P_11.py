"""


Create a function that finds how many prime numbers there are, up to the given
integer.

### Examples

    prime_numbers(10) ➞ 4
    # 2, 3, 5 and 7
    
    prime_numbers(20) ➞ 8
    # 2, 3, 5, 7, 11, 13, 17 and 19
    
    prime_numbers(30) ➞ 10
    # 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29

### Notes

N/A

"""

def prime_numbers(num):
  count=0
  for i in range(2,num+1):
    if prime(i):
      count+=1
  return count
def prime(n):
  if n == 2:
    return True
  else:
    for i in range(2,n):
      if n%i == 0:
        return False
    return True

