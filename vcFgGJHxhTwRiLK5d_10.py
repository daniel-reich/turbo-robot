"""


Given a positive integer `n`, implement a function that finds the **smallest**
number that is evenly divisible by the integers `1` through `n` inclusive.

### Examples

    smallest(1) ➞ 1
    
    smallest(5) ➞ 60
    
    smallest(10) ➞ 2520
    
    smallest(20) ➞ 232792560

### Notes

N/A

"""

from functools import reduce
def is_prime(n):
  ret=True if n>1 else False
  for i in range(2,n//2+1):
    if n%i==0:
      ret=False
      break
  return ret
def primes_factorization(n,pl):
  f=[0]*len(pl)
  for i in range(len(pl)):
    n1=n
    while n1%pl[i]==0:
      f[i]+=1
      n1=n1//pl[i]
  return f
def smallest(n):
  nl=list(range(1,n+1))
  nlp=list(filter(is_prime,nl))
  print(nlp)
  nlpf=[primes_factorization(x,nlp) for x in nl]
  print(nlpf)
  nlpft=[list(x) for x in zip(*nlpf)]
  print(nlpft)
  nlpftmax=[max(x) for x in nlpft]
  pf=[nlp[x]**nlpftmax[x] for x in range(len(nlp))]
  return reduce(lambda x,y: x*y,pf,1)

