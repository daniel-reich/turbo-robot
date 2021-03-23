"""


Create a function that takes a list of factorial expressions and returns the
sum.

### Examples

    eval_factorial(["2!", "3!"]) ➞ 8
    
    eval_factorial(["5!", "4!", "2!"]) ➞ 146
    
    eval_factorial(["0!", "1!"]) ➞ 2

### Notes

0! and 1! both equal 1.

"""

def recup_factorial(L):
  P = list()
  for elt in L:
    P.append(int(elt[:-1]))
  return P
​
def factorial(n):
  S = 1
  for i in range(1,n+1):
    S *=i
  return S
​
​
def eval_factorial(L):
  S = 0
  P = recup_factorial(L)
  for elt in P:
    S += factorial(elt)
  return S

