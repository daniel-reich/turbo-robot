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

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
​
​
def fractions(d):
    p, r = d.find("."), d.find("(")
    whole = (int(d[:p]), 1)
    dec = (int(d[p + 1:r]), 10 ** (r - p - 1)) if r - p > 1 else (0, 1)
    rep = (int(d[r + 1:-1]), (10 ** (len(d) - r - 2) - 1) * 10 ** len(d[p + 1:r]))
    rep = [i / gcd(rep[1], rep[0]) for i in rep]
    e = dec[1] * rep[1] / gcd(dec[1], rep[1])
    f = [whole[0] * e + dec[0] * e / dec[1] + rep[0] * e / rep[1], e]
    return str(int(f[0] / gcd(f[1], f[0]))) + "/" + str(int(f[1] / gcd(f[1], f[0])))

