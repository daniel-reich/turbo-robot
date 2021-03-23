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
    val = []
    l = ['0/1']
    for i in range(1, n+1):
        for j in range(0, n):
            if str(i)+'/'+str(n-j) not in l and i < n-j and i/(n-j) not in val:
                l.append(str(i)+'/'+str(n-j))
                val.append(i/(n-j))
    l2 = l+['1/1']
    return sorted(l2, key=lambda i: eval(i))

