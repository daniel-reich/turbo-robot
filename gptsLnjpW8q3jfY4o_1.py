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

pt = [[1], [1,1]]
for i in range(1, 30):
    r = [1]
    for j in range(1, len(pt[i])):
        r.append(pt[i][j-1] + pt[i][j])
    pt.append(r + [1])
​
def term(c, p, m):
    t = ''
    if c > 1: t += str(c)
    if p > 0: t += 'a' + ('' if p == 1 else '^' + str(p))
    if m > 0: t += 'b' + ('' if m == 1 else '^' + str(m))
    return t
​
def Formula(n):
    if n == 0: return '1'
    positive = n > 0
    n = abs(n)
    m = len(pt[n])
    exp = '+'.join([term(c, m - p - 1, p) for p, c in enumerate(pt[n])])
    return exp if positive else '1/({})'.format(exp)

