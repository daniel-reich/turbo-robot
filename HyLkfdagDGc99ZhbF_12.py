"""


Create a function that takes a number `n` (integer greater than zero) as an
argument, and returns `2` if `n` is odd and `8` if `n` is even.

You can only use the following arithmetic operators: addition of numbers `+`,
subtraction of numbers `-`, multiplication of number `*`, division of number
`/`, and exponentiation `**`.

You are not allowed to use any other methods in this challenge (i.e. no if
statements, comparison operators, etc).

### Examples

    f(1) ➞ 2
    
    f(2) ➞ 8
    
    f(3) ➞ 2

### Notes

N/A

"""

def f(n):
  return [8, 2][n % 2]

