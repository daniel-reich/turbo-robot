"""


You are given a number `n`. Determine whether `n` has exactly **3 divisors**
or not.

### Examples

    is_exactly_three(4) ➞ True
    # 4 has only 3 divisors: 1, 2 and 4
    
    is_exactly_three(12) ➞ False
    # 12 has 6 divisors: 1, 2, 3, 4, 6, 12
    
    is_exactly_three(25) ➞ True
    # 25 has only 3 divisors: 1, 5, 25

### Notes

1 ≤ n ≤ 10^12

"""

def is_exactly_three(n):
    if n<4:return False
    if n<11:
        q=n//2
    else:
        q=int(n**.5)
    k=0
    for i in range(2,q+1):
        if n%i==0:
            k+=1
            if k>1:
                return False
    if k==0:
        return False
    return True

