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

from fractions import Fraction
​
def fractions(decimal):
    d = decimal.replace(')', '').split('(') 
    data = d[0]
    while len(data) < 10:
        data += d[1]
    data = Fraction(float(data)).limit_denominator()
    return str(data.numerator)+"/"+ str(data.denominator)

