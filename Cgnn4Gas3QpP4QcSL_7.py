"""


Create a function that takes an integer parameter, `n`, and returns the sum of
all the digits in each integer in the range 0 to 10^n - 1 inclusive.

  * If `n` is `1`, the range is 0 to 9.
  * if `n` is `2`, the range is 0 to 99.
  * if `n` is `12`, the range is 0 to 999999999999.

`n` will always be `>= 0`. For this challenge, the value of `n` will be
limited to `10000`, but the solution should theoretically work for numbers as
large as `500000`.

### Examples

    sum_digits_in_range(1) ➞ 45
    
    sum_digits_in_range(2) ➞ 900
    
    sum_digits_in_range(3) ➞ 13500
    
    sum_digits_in_range(8) ➞ 3600000000
    
    sum_digits_in_range(13) ➞ 585000000000000

### Notes

  * If `n` is `0`, return `0`.
  * The function must take less than 12 seconds to run.

"""

sum_digits_in_range=lambda n:n*45*10**(n-1)

