"""


Write a function that returns the next number that can be created from the
same digits as the input.

### Examples

    next_number(19) ➞ 91
    
    next_number(3542) ➞ 4235
    
    next_number(5432) ➞ 5432
    
    next_number(58943) ➞ 59348

### Notes

  * If no larger number can be formed, return the number itself.
  *  **Bonus** : See if you can do this without generating all digit permutations.

"""

def next_number(n):
    if n < 10:
        return n
    digs = [int(x) for x in str(n)]
    i = len(digs)-2
    while i >= 0 and digs[i] >= digs[i+1]:
        i-=1
    if i >= 0:
        k = digs[i]
        # bin search
        l, r = i+1, len(digs)-1
        while l < r - 1:
            m = (l+r)//2
            if digs[m] <= k:
                r = m
            else:
                l = m
        j = l
        if l == r-1 and digs[r] > k:
            j = r
        digs[i], digs[j] = digs[j], digs[i]
        digs[i+1:] = digs[len(digs)-1:i:-1]
        return int(''.join(str(x) for x in digs))
    return n

