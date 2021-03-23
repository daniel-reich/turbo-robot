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

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a
​
def reduce(fraction):
    num, den = [int(i) for i in fraction.split("/")]
    while gcd(num, den) > 1:
        g = gcd(num, den)
        num //= g
        den //= g
    return str(num)+"/"+str(den)
    
​
def farey(n):
    lst = ["0/1"] + [str(i)+"/"+str(j) for i in range(1,n) for j in range(1,n+1) if i<=j]
    lst = [reduce(i) for i in lst]
    return sorted(list(set(lst)), key = eval)

