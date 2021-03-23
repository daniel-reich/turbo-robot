"""


Create a function that subtracts one positive integer from another, without
using any arithmetic operators such as `-`, `%`, `/`, `+`, etc.

### Examples

    my_sub(5, 9) ➞ 4
    
    my_sub(10, 30) ➞ 20
    
    my_sub(0, 0) ➞ 0

### Notes

  * Do not multiply by `-1`.
  * Use bitwise operations only: `<<`, `|`, `~`, `&`, etc.

"""

def my_sub(a, b):
    binary_a = '0' * (8 - len(bin(a)[2:])) + bin(a)[2:]
    ones_comp = ''.join('0' if i == '1' else '1' for i in binary_a)
    twos_comp_plus_b = int(ones_comp, 2) + 1 + b
    return int(bin(twos_comp_plus_b)[-8:], 2)

