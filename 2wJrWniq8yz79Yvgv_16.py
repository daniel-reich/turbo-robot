"""


A [Narcissistic Number](https://en.wikipedia.org/wiki/Narcissistic_number) is
a number that is the sum of its own digits each raised to the power of the
number of digits.

For example, take 153 (3 digits), which is narcisstic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

1652 (4 digits), is non-narcisstic:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938

Create a function which returns `True` or `False` depending upon whether the
given number `n` is a Narcissistic number or not.

### Examples

    is_narcissistic(153) ➞ True
    
    is_narcissistic(370) ➞ True
    
    is_narcissistic(1652) ➞ False

### Notes

N/A

"""

def is_narcissistic(n):
    return sum(int(i)**len(str(n)) if len(str(n))>1 else int(i) for i in str(n))==n

