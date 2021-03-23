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

def divisor_sum(n):
  return sum(i for i in range (1,1+n//2) if n%i==0)
​
def num_type(n):
  x = divisor_sum(n)
  if x==n:
    return "Perfect"
  if divisor_sum(x)==n:
    return "Amicable"
  return "Neither"

