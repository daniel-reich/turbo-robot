"""


Adding fractional binary numbers is similar to adding decimals. The places to
the right of the decimal point (or binary point) are halves, quarters, eighths
instead of tenths, hundredths, thousandths, etc.

Improvise a function that takes two fractional binary numbers and produces
their base-10 sum. The sum can be a whole number, a fraction, or a mixed
number. The answer should be returned as a string with fractions reduced to
lowest terms.

### Examples

    binary_sum(["1.1", "1.1"]) ➞ "3"
    # 1.5 + 1.5
    
    binary_sum(["11.1", "0.001"]) ➞ "3 5/8"
    # 3.5 + 0.125
    
    binary_sum(["1101.0", "0.0100"]) ➞ "13 1/4"
    # 13 + 1/4
    
    binary_sum(["0.11", "0.00001"]) ➞ "25/32"
    # 3/4 + 1/32
    
    binary_sum(["0.0", "101.00"]) ➞ "5"

### Notes

N/A

"""

def binary_sum(lst):
    sum=0
    lst=[lst[0].strip('0'),lst[1].strip('0')]
    d=[len(lst[0])-lst[0].find('.'), len(lst[1])-lst[1].find('.')]
    denom=2**(max(d)-1)
    for k in range(2):
        for i in range(-1,-len(lst[k])-1,-1):
            if lst[k][i]!='.':
                d[k]-=1
                sum+=int(lst[k][i])*(1/2**(d[k]))*denom
    whole=int(sum//denom)
    numer=int(sum%denom)
    if whole>0 and numer>0:
        return '{} {}/{}'.format(whole,numer,denom)
    if numer>0:
        return '{}/{}'.format(numer,denom)
    return str(whole)

