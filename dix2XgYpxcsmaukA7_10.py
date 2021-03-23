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

import math
def express_factors(n):
    x = []
    while n % 2 == 0:
        x.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            x.append(int(i))
            n = n / i
    if n > 2:
        x.append(int(n))
    y,res=[],''
    for i,v in enumerate(x):
        count=x.count(v)
        if (v, x.count(v))not in y:
            y.append((v,count))        
    for i in y:
        if i[1]>1:
            res+=str(i[0])+'^'+str(i[1])+' '+'x'+' '
        else: 
            res+=str(i[0])+' '+'x'+' '
    return res[0:-2].strip()

