"""


Create a function that takes a integer number `n` and returns the formula for
`(a+b)^n` as a string.

### Examples

    Formula(0) ➞ "1"
    
    Formula(1) ➞ "a+b"
    
    Formula(2) ➞ "a^2+2ab+b^2"
    
    Formula(-2) ➞ "1/(a^2+2ab+b^2)"
    
    Formula(3) ➞ "a^3+3a^2b+3ab^2+b^3"
    
    Formula(5) ➞ "a^5+5a^4b+10a^3b^2+10a^2b^3+5ab^4+b^5"

### Notes

Don't put the following in your string:

  * `spaces`
  * `*`
  * `^1`
  * `a^0`
  * `b^0`

"""

import math
​
def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
​
def Formula(n):
    if n == 0:
        return "1"
    ans = ""
    negative = False
    if n < 0:
        negative = True
        ans += "1/("
        n = -n
    for k in range(n, -1, -1):
        coeff = binomial_coefficient(n, k)
        if coeff > 1:
            ans += str(coeff)
        if k > 0:
            ans += "a"
        if k > 1:
            ans += "^" + str(k)
        if k < n:
            ans += "b"
        if k < n - 1:
            ans += "^" + str(n - k)
        if k > 0:
            ans += "+"
    if negative:
        ans += ")"
    return ans

