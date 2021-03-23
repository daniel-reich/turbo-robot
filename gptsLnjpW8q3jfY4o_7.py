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

def Formula(n):
    if not n: return '1'
    Formula, sign, res = str(), n < 0, 1
    if sign: n = -n
    for i in range(n + 1):
        if i % n: 
            res = int(res * (n - i + 1) / i)
            Formula += str(res)
        if i < n: Formula += 'a'
        if i < n - 1: Formula += '^' + str(n - i)
        if i > 0: Formula += 'b'
        if i > 1: Formula += '^' + str(i)
        if i < n: Formula += '+'
    return ('1/(' + Formula + ')' if sign else Formula)

