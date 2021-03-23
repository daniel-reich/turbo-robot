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

import re
from decimal import Decimal
from fractions import Fraction
​
def fractions(dec):
    # decimal preprocessing
    decGroups = re.search(r'(\d+)\.(\d+)?\((\d+)\)', dec)
    dec = [
        decGroups.group(1),
        decGroups.group(2),
        decGroups.group(3)
    ]
​
    # find the length of repeated segment
    repeated = len(dec[2])
​
    # there is a non-repeated segment
    if dec[1]:
        # create numerator subtrahend
        nonRepeated = len(dec[1])
        numSub = dec[0] + '.'.join(dec[1:])
​
    else:
        # remove empty entry
        del dec[1]
​
        # create numerator subtrahend
        nonRepeated = 0
        numSub = '.'.join(dec)
​
    # create numerator minuend
    numMin = '{0}.{1}'.format(''.join(dec), dec[-1])
​
    # convert to decimal obj
    numMin = Decimal(numMin)
    numSub = Decimal(numSub)
​
    # create denominator minuend and subtrahend
    denomMin = 10 ** (repeated + nonRepeated)
    denomSub = 10 ** nonRepeated
​
    # create numerator and denominator
    num = int(numMin - numSub)
    denom = denomMin - denomSub
​
    # reduce fraction
    fraction = Fraction(num, denom)
    num = fraction.numerator
    denom = fraction.denominator
​
    # return fraction
    return '{0}/{1}'.format(num, denom)

