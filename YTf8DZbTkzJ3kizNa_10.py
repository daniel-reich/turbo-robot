"""
A **Harshad** number is a number which is divisible by the sum of its digits.
For example, 132 is divisible by 6 (1+3+2).

A subset of the Harshad numbers are the **Moran** numbers. Moran numbers yield
a prime when divided by the sum of their digits. For example, 133 divided by 7
(1+3+3) yields 19, a prime.

Create a function that takes a number and returns `"M"` if the number is a
Moran number, `"H"` if it is a (non-Moran) Harshad number, or `"Neither"`.

### Examples

    moran(132) ➞ "H"
    
    moran(133) ➞ "M"
    
    moran(134) ➞ "Neither"

### Notes

N/A

"""

def is_prime(num):
    if num == 0 or num == 1:
        return False
    if num == 2 or num == 3:
        return True
    for num_1 in range(2, num // 2 + 1):
        if num % num_1 == 0:
            return False
    return True
​
def moran(n):
    if (n % sum(int(num) for num in str(n))) == 0 and is_prime(n // sum(int(num) for num in str(n))):
        return "M"
    elif (n % sum(int(num) for num in str(n))) == 0 and not is_prime(n // sum(int(num) for num in str(n))):
        return "H"
    else:
        return "Neither"

