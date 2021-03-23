"""


Create a function that takes an integer `n` and returns the **factorial of
factorials**. See below examples for a better understanding:

### Examples

    fact_of_fact(4) ➞ 288
    # 4! * 3! * 2! * 1! = 288
    
    fact_of_fact(5) ➞ 34560
    
    fact_of_fact(6) ➞ 24883200

### Notes

N/A

"""

def fact_of_fact(n):
    if n == 1:
        return 1
    f = [1]
    a = 0
    for i in range(2,n+1):
        f.append(i*f[a])
        a += 1
    myans = 1
    for i in f:
        myans *= i
    return myans

