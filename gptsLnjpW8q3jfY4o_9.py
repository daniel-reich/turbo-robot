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

from math import factorial
​
def Formula(n):
    if n == 0:
        return "1"
    sol = []
    m = abs(n)
    fact = 0
    x = 0
    for k in range(m+1):
        fact = factorial(m)//(factorial(k)*factorial(m-k))
        x = m - k
        sol.append("{}{}{}{}{}{}{}".format("" if fact == 0 or fact == 1 else fact, "" if x ==
                                           0 else "a", "" if x < 2 else "^", "" if x < 2 else x, "" if k ==
                                           0 else "b", "" if k < 2 else "^", "" if k < 2 else k))
    return "1/({})".format("+".join(sol)) if n < 0 else "+".join(sol)

