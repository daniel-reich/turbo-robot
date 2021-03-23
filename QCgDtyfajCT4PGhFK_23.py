"""


Write a function that returns the extended form of the prime factorization of
a number. Return in the format `[a, b, c, d, ...]`, where each element of the
list is an integer.

### Examples

    prime_factorization(216) ➞ [2, 2, 2, 3, 3, 3]
    
    prime_factorization(64) ➞ [2, 2, 2, 2, 2, 2]
    
    prime_factorization(23) ➞ [23]

### Notes

N/A

"""

def prime_factorization(n):
  ans=[]
  while n%2==0:
    ans.append(2)
    n=n//2
  for i in range(3,n+1,2):
    if n%i==0:
      ans.append(i)
      n=n//i
  if n>2:ans.append(n)
  return sorted(ans)

