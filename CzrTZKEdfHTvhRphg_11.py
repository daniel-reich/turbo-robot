"""


Create a function that takes a string representing a fraction, and return a
string representing that input as a mixed number.

  * Mixed numbers are of the form `1 2/3` — note the space between the whole number portion and the fraction portion.
  * Resulting fractions should be fully reduced (see example #2).
  * If a result is a whole number with no fractional remainder, return only the whole number portion (see example #3).
  * If a result is only fractional with no whole number, return only the fractional portion (see example #4).
  * If a result is negative, the whole number should carry the negative sign. If the result would not have a whole number portion, the numerator of the fractional portion should carry the negative sign (see examples #5 - #7).

### Examples

    mixed_number("5/4") ➞ "1 1/4"
    
    mixed_number("6/4") ➞ "1 1/2"
    
    mixed_number("8/4") ➞ "2"
    
    mixed_number("4/6") ➞ "2/3"
    
    mixed_number("-1/4") ➞ "-1/4"
    
    mixed_number("-5/4") ➞ "-1 1/4"
    
    mixed_number("-8/4") ➞ "-2"

### Notes

All provided inputs will be formatted similarly, negative numbers will be
provided in the numerator portion only, and all inputs will contain no spaces,
invalid characters, or zero denominators.

"""

def gcd(d,n):
    while d%n!=0:
        rem=d%n
        d=n
        n=rem
    return n
​
​
def reducefrac(frac_p):
    while gcd(int(frac_p[frac_p.index('/')+1:]),int(frac_p[0:frac_p.index('/')]))!=1:
        n,d=int(frac_p[0:frac_p.index('/')]),int(frac_p[frac_p.index('/')+1:])
        frac_n=str(n//gcd(d,n))
        frac_d=str(d//gcd(d,n))
        frac_p=frac_n+'/'+frac_d
    return frac_p
​
​
​
def mixed_number(frac):
    if frac[0]=='-':
        frac=frac[1:]
        sign='-'
    else:
        sign=''
​
    numerator=int(frac[0:frac.index('/')])
    denominator=int(frac[frac.index('/')+1:])
    whole_p=str(numerator//denominator)+' '
    frac_p=str(numerator%denominator)+ '/' +str(denominator)
    if whole_p=='0 ':
        whole_p=''
    if frac_p[0:frac_p.index('/')]=='0':
        frac_p=''
        whole_p=whole_p[0:len(whole_p)-1]
    if frac_p!='':
        if gcd(int(frac_p[0:frac_p.index('/')]),int(frac_p[frac_p.index('/')+1:]))!=1:
            frac_p=reducefrac(frac_p)
    res=sign+whole_p+frac_p
    if res=='':
        res='0'
    return res

