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

import itertools
def maxmin(n):
    res=[n]
    n=list(str(n))
    for i in itertools.permutations(range(len(n)),2):        
        new_num=n[:]        
        new_num[int(i[0])]=n[int(i[1])]
        new_num[int(i[1])]=n[int(i[0])]
        if new_num[0]!="0":
            res.append(int("".join(new_num)))    
    return (max(res),min(res))

