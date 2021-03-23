"""


Maxie is the largest number that can be obtained by **swapping two digits** ,
Minnie is the smallest. Write a function that takes a number and returns Maxie
and Minnie. Leading zeros are not permitted.

### Examples

    maxmin(12340) ➞ (42310, 10342)
    
    maxmin(98761) ➞ (98761, 18769)
    
    maxmin(9000) ➞ (9000, 9000)
    # Sometimes no swap needed.
    
    maxmin(11321) ➞ (31121, 11123)

### Notes

N/A

"""

def maxmin(n):
    digits = [int(d) for d in str(n)]
    l = len(digits)
    minie = n
    maxie = n
    for i in range(l):
        for j in range(i + 1, l):
            d1, d2 = digits[i], digits[j]
            num = digits[:]
            num[i] = d2
            num[j] = d1
            if num[0] != 0:
                k = int(''.join(map(str, num)))
                minie = min(minie, k)
                maxie = max(maxie, k)
    return (maxie, minie)

