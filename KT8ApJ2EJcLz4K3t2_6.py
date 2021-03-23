"""


For this challenge, you are supposed to find the sum of the digits of a two-
digit number. Sounds easy, right? But for this challenge, I expect you to find
the sum of the digits mathematically.

Sure, you can convert the number into a string and then manipulate it so it
returns the sum of the digits, but the point of this challenge is to see if
you know how to return the sum of the digits of a two-digit number
**mathematically**.

### Examples

    two_digit_sum(45) ➞ 9
    
    two_digit_sum(38) ➞ 11
    
    two_digit_sum(67) ➞ 13

### Notes

`%` `//`

"""

def two_digit_sum(n):
    return sum(divmod(n, 10))

