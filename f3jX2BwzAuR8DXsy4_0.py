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
    f = count = 1
    for i in range(1, n + 1):
        f *= i
        count *= f
    return count

