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
    def my_min(lst, index):
        mi = 9
        if index == 0:
            for x in lst:
                if 0 < x < mi:
                    mi = x
        else:
            for x in lst:
                if 0 <= x < mi:
                    mi = x
        return mi
    n_max = [int(x) for x in str(n)]
    n_min = n_max.copy()
    n = list(reversed(n_max))
    for x in range(len(n)-1):
        if max(n_max[x+1:]) > n_max[x]:
            i = n_max[x]
            n_max[x] = max(n_max[x+1:])
            n_max[-1*n.index(max(n_max[x+1:]))-1] = i
            break
    for x in range(len(n)-1):
        if 0 <= my_min(n_min[x+1:], x) < n_min[x]:
            i = n_min[x]
            n_min[x] = my_min(n_min[x+1:], x)
            n_min[-1*n.index(my_min(n_min[x+1:], x))-1] = i
            break
    return (int(''.join([str(x) for x in n_max])), int(''.join([str(x) for x in n_min])))

