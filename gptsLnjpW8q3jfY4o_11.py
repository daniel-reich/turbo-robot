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

def binomial_seq(n):
    if n == 0:
        return []
    seq = [1, 1]
    for k in range(2, n + 1):
        new_seq = [1] * (k + 1)
        for i in range(1, k):
            new_seq[i] = seq[i] + seq[i - 1]
        seq = new_seq
    return seq
​
​
def Formula(n):
    if n == 0:
        return '1'
    n_positive = True
    if n < 0:
        n_positive = False
        n *= -1
    if n == 1:
        res = 'a+b'
    else:
        cfs = binomial_seq(n)
        res = 'a^{}'.format(n)
        for i in range(1, n):
            res += ('+{}a{}b{}'
                    .format(cfs[i], '^{}'.format(n - i) if (n - i) > 1 else '',
                            '^{}'.format(i) if i > 1 else ''))
        res += '+b^{}'.format(n)
    return res if n_positive else '1/({})'.format(res)

