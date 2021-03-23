"""


Create a function that filters out factorials from a list. A factorial is a
number that can be represented in the following manner:

    n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

Recursively, this can be represented as:

    n! = n * (n-1)!

### Examples

    filter_factorials([1, 2, 3, 4, 5, 6, 7]) ➞ [1, 2, 6]
    
    filter_factorials([1, 4, 120]) ➞ [1, 120]
    
    filter_factorials([8, 9, 10]) ➞ []

### Notes

N/A

"""

def filter_factorials(numbers):
    numbers2 = []
    f = []
    def factorial(num):
        if num == 1:
            return num
        return factorial(num - 1) * num
    for i in range(1,10):
        numbers2.append(factorial(i))
    for i in numbers:
        if i in numbers2:
            f.append(i)
    return f

