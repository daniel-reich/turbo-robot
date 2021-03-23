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

def reduce(frac):
    nums = frac.split('/')
    numer = int(nums[0])
    denom = int((nums[1]))
​
    for i in range(2, denom + 1):
        while numer % i == 0 and denom % i == 0:
            numer, denom = int(numer / i), int(denom / i)
        
    return str(numer) + '/' + str(denom)
​
print(reduce('100/100'))
​
def farey(num):
    out = ['0/1']
    for i in range(num + 1):
        for a in range(1, i + 1):
            string = str(a) + '/' + str(i)
            if reduce(string) not in out:
                out.append(reduce(string))
    out = sorted(out, key = sortKey)
    return out
def sortKey(frac):
    nums = frac.split('/')
    numer = int(nums[0])
    denom = int((nums[1]))
    return numer / denom

