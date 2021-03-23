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

from math import factorial as f
def Formula(n):
  r = True if n < 0 else False
  n = abs(n)
  e = [str(f(n)//(f(i)*f(n-i))) + 'a^'+str(n-i) + 'b^'+str(i) for i in range(n+1)]
  e = 'X' + '+'.join(e) + 'X'
  e = e.replace('a^1b', 'ab').replace('b^1+', 'b+').replace('b^1X', 'b')
  e = e.replace('a^0', '').replace('b^0', '')
  e = e.replace('X1a', 'a').replace('+1b', '+b').replace('X', '')
  return  '1/(' + e + ')' if r else e

