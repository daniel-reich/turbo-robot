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

def sum_of_posi_div(n):
    return sum([i for i in range(1, n) if not n % i])
​
​
def num_type(n):
    if sum_of_posi_div(n) == n:
        return 'Perfect'
    elif n == sum_of_posi_div(sum_of_posi_div(n)):
        return 'Amicable'
    else:
        return 'Neither'
​
​
print(num_type(6))
print(num_type(2924))
print(num_type(5010))

