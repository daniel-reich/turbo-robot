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

factorial = lambda n: eval('*'.join([str(i) for i in reversed(range(1, n+1))]))
fact_of_fact = lambda n: eval('*'.join([str(factorial(i)) for i in reversed(range(1, n+1))]))

