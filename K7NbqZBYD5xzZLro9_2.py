"""


Create a function that takes a range of numbers and returns the sum of each
digit from `start` to `stop`.

### Examples

    digits_sum(1, 10) ➞ 46
    # total numbers in the range are = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # sum of each digits is = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 1 + 0 = 46
    
    digits_sum(1, 20) ➞ 102
    
    digits_sum(1, 100) ➞ 901

### Notes

`start` and `stop` are inclusive in the range.

"""

from math import*
def f(n):
    if n<10:return n*(n+1)/2
    d=(int)(log10(n))
    a=[0]*(d+1)
    a[0:2]=[0,45]
    for i in range(2,d+1):a[i]=a[i-1]*10+45*ceil(10**(i-1))
    p=ceil(10**d)
    m=n//p
    return(int)(m*a[d]+(m*(m-1)//2)*p+m*(1+n%p)+f(n%p))
digits_sum=lambda b,e:f(e)-f(b-1)

