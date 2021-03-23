"""


The Farey sequence of order `n` is the set of all fractions with a denominator
between 1 and `n`, reduced and returned in ascending order. Given `n`, return
the Farey sequence as a list, with each fraction being represented by a string
in the form "numerator/denominator".

### Examples

    farey(1) ➞ ["0/1", "1/1"]
    
    farey(4) ➞ ["0/1", "1/4", "1/3", "1/2", "2/3", "3/4", "1/1"]
    
    farey(5) ➞ ["0/1", "1/5", "1/4", "1/3", "2/5", "1/2", "3/5", "2/3", "3/4", "4/5", "1/1"]

### Notes

The Farey sequence will always begin with "0/1" and end with "1/1".

"""

from fractions import Fraction
​
def farey(n):
    m = 2*n if n % 2 == 0 else 2*n+2
    f = []
    fraclist = []
    
    for den in range(2,n+1):
        for num in range(1,den):
            if not Fraction(str(num) + '/' + str(den)) in fraclist:
                fraclist.append(Fraction(str(num) + '/' + str(den)))
    
    f.append('0/1')
    while len(fraclist) > 0:
        f.append(str(fraclist[fraclist.index(min(fraclist))]))
        fraclist.pop(fraclist.index(min(fraclist)))
    f.append('1/1')
    
    return f

