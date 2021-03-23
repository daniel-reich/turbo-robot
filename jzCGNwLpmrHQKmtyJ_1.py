"""


Create a function that takes a number as input and returns `True` if the sum
of its digits has the same parity as the entire number. Otherwise, return
`False`.

### Examples

    parity_analysis(243) ➞ True
    # 243 is odd and so is 9 (2 + 4 + 3)
    
    parity_analysis(12) ➞ False
    # 12 is even but 3 is odd (1 + 2)
    
    parity_analysis(3) ➞ True
    # 3 is odd and 3 is odd and 3 is odd (3)

### Notes

  * Parity is whether a number is even or odd. If the sum of the digits is even and the number itself is even, return `True`. The same goes if the number is odd and so is the sum of its digits.
  * Single digits will obviously have the same parities (see example #3).

"""

def parity_analysis(num):
  return num % 2 == sum(int(i) for i in str(num)) % 2

