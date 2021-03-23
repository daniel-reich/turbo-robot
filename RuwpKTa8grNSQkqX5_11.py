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
from fractions import Fraction
​
def fractions(decimal):
    i, f, p = re.match(r'(\d+)\.(\d*)\((\d+)\)', decimal).groups()
    pow1, pow2 = 10**len(f), 10**len(p)
    i, f, p = int(i), int(f or '0'), int(p)
    print(i,f,p)
    return str(Fraction(f, pow1) + Fraction(p, pow1 * (pow2-1)) + i)

