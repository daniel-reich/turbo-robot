"""


Create a function that takes a positive integer and returns a string
expressing how the number can be made by multiplying powers of its prime
factors.

### Examples

    express_factors(2) ➞ "2"
    
    express_factors(4) ➞ "2^2"
    
    express_factors(10) ➞ "2 x 5"
    
    express_factors(60) ➞ "2^2 x 3 x 5"

### Notes

  * All inputs will be positive integers in the range 1 < n < 10,000.
  * If a factor is repeated express it in the form **"x^y"** where x is the factor and y is the number of repetitions of the factor.
  * If `n` is a prime number, return `n` as a string as in example #1 above.
  * Factors should appear in ascending order in the expression.
  * Make sure you include the space either side of the multiplication sign, `" x "`.
  * Check the **Resources** if you need to understand **Prime Factorization**.

"""

def is_prime(n):
  return n>1 and all(n%i for i in range(2, int(n**0.5)+1))
def express_factors(n):
  A=[x for x in range(2, n+1) if n%x==0 and is_prime(x)]
  B=[]
  for x in A:
    i=0
    while n%x**i==0:
      i+=1
    B.append((x,i-1))
  C=[str(x[0])+'^{}'.format(x[1])*(x[1]!=1)  for x in B]
  return ' x '.join(C)

