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

def num_type(number):
    
    divisor_sum = calculate_divisor(number)
    
    if divisor_sum == number:
        return "Perfect"
    
    if divisor_sum != number:
        divisor_sum2 = calculate_divisor(divisor_sum)
        if divisor_sum2 == number:
            return "Amicable"
        else:
            return "Neither"
​
def calculate_divisor(listing):
    positive_divisor = []
    for num in range(1,listing):
        if listing % num == 0:
            positive_divisor.append(num)
    return sum(positive_divisor)

