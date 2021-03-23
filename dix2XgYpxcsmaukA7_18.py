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

prime = []
for i in range(2,10000):
  b = 0
  for j in range(2,100):
    if j**2<=i:
      if i%j==0:
        b+=1
  if b==0:
    prime.append(i)
def express_factors(n):
    ans = []
    k = 0
    if n not in prime:
        for i in prime:
            for j in range(1,15):
                if n%(i**j)==0:
                    if j==1:
                        k = i
                    else:
                        k = str(str(i) + '^' + str(j))
            if k!=0 and k not in ans:
                ans.append(k)
    else:
        ans.append(n)
    d = str()
    for i in ans:
        if i==ans[0]:
            d = str(i)
        else:
            d = d + ' x ' + str(i)
    return d

