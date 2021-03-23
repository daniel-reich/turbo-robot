"""


Performing division on a fraction often results in an infinitely repeating
decimal.

    1/3=.3333333...  1/7=.142857142857...

Create a function that takes a decimal in string form with the repeating part
in parentheses and returns the equivalent fraction in string form and in
lowest terms.

### Examples

    fractions("0.(6)") ➞ "2/3"
    
    fractions("1.(1)") ➞ "10/9"
    
    fractions("3.(142857)") ➞ "22/7"
    
    fractions("0.19(2367)") ➞ "5343/27775"
    
    fractions("0.1097(3)") ➞ "823/7500"

### Notes

N/A

"""

from fractions import gcd
def fractions(decimal):
    d,l = decimal.index('.'), decimal.index('(')
    bd, ad, rp = decimal[:d], decimal[d+1:l], decimal[l+1:-1]
    den = 10**(len(ad)+len(rp)) - 10**int(len(ad))
    num = int(bd+ad+rp) - int(bd+ad)
    g = gcd(den, num)
    return '{}/{}'.format(num//g, den//g)

