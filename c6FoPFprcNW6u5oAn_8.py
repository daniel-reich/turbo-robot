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

def farey(n):
    l = []
    for k in range(1,n):
        for j in range(k+1,n+1):
            i,x,y = k,k,j
            while y != 0:
                (x, y) = (y, x % y)
            i /= x; i = int(i); j /= x; j = int(j)
            l.append(("/".join(map(str,[i,j]))))
    return ["0/1"] + sorted(set(l),key = eval) + ["1/1"]

