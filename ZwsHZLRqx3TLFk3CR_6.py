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

import re
​
​
def eval_factorial(*lst):
    sum = 0
    nums = []
    num = 1
    fac = 1
    for n1 in lst:
        n1 = re.sub('!', '', str(n1))
        n1 = n1.replace('[', '')
        n1 = n1.replace(']', '')
        n1 = n1.replace("'", '')
        print(n1)
        for n in n1.split(','):
            for i in range(int(n)):
                num *= fac
                fac += 1
            nums.append(num)
            fac = 1
            num = 1
    for n in nums:
        sum += n
    return sum

