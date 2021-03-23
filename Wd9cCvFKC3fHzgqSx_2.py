"""


Create a function that takes a number `num` and returns each place value in
the number.

### Examples

    num_split(39) ➞ [30, 9]
    
    num_split(-434) ➞ [-400, -30, -4]
    
    num_split(100) ➞ [100, 0, 0]

### Notes

N/A

"""

def num_split(num):
  n = list(str(abs(num)))
  res = [int(n[i])  * int("1" + "0" * (len(n) - i - 1)) for i in range(len(n))]
  return res if num > 0 else [-i for i in res]

