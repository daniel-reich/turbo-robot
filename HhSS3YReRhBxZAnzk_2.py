"""


Python's range function can only generate a list of integers, your task is to
generate a list of floats. Generate a list of values between 0 and an endpoint
`n` spaced at `i` intervals.

### Examples

    gen_values(2, 0.25) ➞ [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
    
    gen_values(1, 0.1) ➞ [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    
    gen_values(20, 2) ➞ [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

### Notes

  * The endpoint will always be a positive integer.
  * This function should also work for generating integers (last example).

"""

def gen_values(n, i):
  return [round(i * j, 10) for j in range(int(n / i) + 1)]

