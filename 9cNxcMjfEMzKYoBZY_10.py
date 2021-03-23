"""


Given a positive number x, if all the positive divisors of x (excluding x) add
up to x, then x is said to be a perfect number.

For example, the set of positive divisors of 6 excluding 6 itself is (1, 2,
3). The sum of this set is 6. Therefore, 6 is a _perfect_ number.

Given a positive number x, if all the positive divisors of x add up to a
second number y, and all the positive divisors of y add up to x, then x and y
are said to be a pair of _amicable_ numbers.

Create a function that takes a number and returns `"Perfect"` if the number is
perfect, `"Amicable"` if the number is part of an amicable pair, or
`"Neither"`.

### Examples

    num_type(6) ➞ "Perfect"
    
    num_type(2924) ➞ "Amicable"
    
    num_type(5010) ➞ "Neither"

### Notes

N/A

"""

def num_type(n):
    sum1=0
    sum2=0
    for i in range(1,n):
        if n%i==0:
            sum1+=i
    print(sum1)
    if sum1==n:
        return "Perfect"
    elif sum1!=n:
        for i in range(1,sum1):
            if sum1%i==0:
                sum2+=i
    if sum2==n:
        return "Amicable"
    else:
        return "Neither"

