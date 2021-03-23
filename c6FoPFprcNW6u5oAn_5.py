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
    lst = ["0/1"]
    secondlst = [0]
    for i in range(1, n + 1):
        for o in range(1, i):
            if round(o / i, 10) in secondlst:
                continue
            else:
                lst.append(str(o) + "/" + str(i))
                secondlst.append(round(o / i, 10))
    sortedlst = [x for _, x in sorted(zip(secondlst, lst))]
    sortedlst.append("1/1")
    return sortedlst

