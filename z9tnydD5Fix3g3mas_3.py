"""


Create a function that checks if the sub-lists in a list adhere to the
specified pattern.

### Examples

    check_pattern([[1, 1], [2, 2], [1, 1], [2, 2]], "ABAB") ➞ True
    
    check_pattern([[1, 2], [1, 3], [1, 4], [1, 2]], "ABCA") ➞ True
    
    check_pattern([[1, 2, 3], [1, 2, 3], [3, 2, 1], [3, 2, 1]], "AABB") ➞ True
    
    check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "ABCD") ➞ True
    
    check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "DCBA") ➞ True

### Notes

  * The length of the pattern will always be the same as the length of the (main) list.
  * The pattern does not necessarily have to be alphabetically ordered (see last example).

"""

def check_pattern(lst, p):
    t='ABCD'
    for i in t:
        d=[]
        e=[0,1,2,3]
        n=p.count(i)
        k=0
        for j in range(n):
            m=p.find(i,k)
            d.append(m)
            e.remove(m)
            k=m+1
        if len(d)>1:
            for j in range(len(d)-1):
                if lst[d[j]]!=lst[d[j+1]]:
                    return False
                for f in e:
                    if lst[d[j]]==lst[f]:
                        return False
    return True

