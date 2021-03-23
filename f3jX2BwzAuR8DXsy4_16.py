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

fac = {0: 1, 1: 1}
f = 1
for k in range(2, 51):
    f *= k
    fac[k] = f
​
def fact_of_fact(n):
    ans = 1
    for k in range(2, n + 1):
        ans *= fac[k]
    return ans

