"""


Imagine you took all the numbers between 0 and `n` and concatenated them
together into a long string. How many digits are there between 0 and `n`?
Write a function that can calculate this.

There are 0 digits between 0 and 1, there are 9 digits between 0 and 10 and
there are 189 digits between 0 and 100.

### Examples

    digits(1) ➞ 0
    
    digits(10) ➞ 9
    
    digits(100) ➞ 189
    
    digits(2020) ➞ 6969

### Notes

The numbers are going to be rather big so creating that string won't be
practical.

"""

def digits(num):
    x = len(str(num)) - 1
    digits_ = x * pow(10, x) + (1 - pow(10, x)) // 9
    rest_digits = (num - 10 ** x) * len(str(pow(10, x)))
    return digits_ + rest_digits

