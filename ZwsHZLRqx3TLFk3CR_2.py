"""


Create a function that takes a list of factorial expressions and returns the
sum.

### Examples

    eval_factorial(["2!", "3!"]) ➞ 8
    
    eval_factorial(["5!", "4!", "2!"]) ➞ 146
    
    eval_factorial(["0!", "1!"]) ➞ 2

### Notes

0! and 1! both equal 1.

"""

def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fact(n-1)*n
​
def eval_factorial(lst):
    myans = 0
​
    for i in range(len(lst)):
        myans += fact(int(lst[i][:-1]))
​
    return myans

