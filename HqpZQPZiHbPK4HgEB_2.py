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
    n = str(n)
    x = [(x,y) for x in range(len(n)) for y in range(len(n))]
    z = []
    for i in x:
        n0 = list(n)
        n0[i[0]], n0[i[1]] = n0[i[1]], n0[i[0]]
        z += [(''.join(n0))]
    z = [int(x) for x in z if x[0] != '0']
    return(max(z), min(z))

