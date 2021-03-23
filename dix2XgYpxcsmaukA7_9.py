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

def prime_factors(n):
    i=1;primes=[]
    while i*i<n:
        i+=1
        while n%i==0:
            primes.append(i)
            n//=i
    if n>1:primes.append(n)
    return primes   
def express_factors(n):
    ans=''
    p=prime_factors(n)
    ps=sorted(list(set(p)))
    for i in ps:
        k=p.count(i)
        if k>1:
            ans+=str(i)+'^'+str(k)+' x '
        else:
            ans+=str(i)+' x '
    return ans[:-3]

