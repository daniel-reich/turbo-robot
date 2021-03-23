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

from math import factorial
def eval_factorial(lst):
    ev=0
    for i in lst:
        if i =="0!" or i== "1! ":
            ev+=1
        else:
            ev+=factorial(int(i.strip("!")))
    return ev

