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
    r = ["0/1", "1/1"]
    for x in range(1, n):
        for y in range(n, x, - 1):
            k = any([x % i == y % i == 0 for i in range(2, y + 1)])
            if x != y and not k:
                add = str(x) + "/" + str(y)
                r.append(add)
    return sorted(r, key=lambda x : eval(x))

