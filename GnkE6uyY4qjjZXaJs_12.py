"""


Create a function that takes a positive integer `n` and returns the `n`th
"star number".

A star number is a centered figurate number a centered hexagram (six-pointed
star), such as the one that Chinese checkers is played on.

### Examples

    star_number(2) ➞ 13
    # n = 2
    # 2nd star number = 13
    
    star_number(3) ➞ 37
    # n = 3
    # 3rd star number = 13
    
    star_number(5) ➞ 121
    # n = 3
    # 5th star number = 13

### Notes

  * `n` will always be a positive integer.
  * The `n`th term of a star number can be represented as `6n(n-1) + 1`
  * See **Resources** for more information.

"""

def star_number(n):
  return (6 * n * (n-1)+1)

