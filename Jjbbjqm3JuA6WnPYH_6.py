"""


Python offers some bit operations but not bit rotation. To complete that,
create a function that takes three parameters:

  1. `n`: Integer, which in binary representaion should be rotated.
  2. `m`: Number of rotation steps that should be performed.
  3. `d`: Boolean value; `True` = rotation right, `False` = rotation left.

Your function should return an integer as a result of its rotated binary
representation.

### Examples

    bit_rotate(8, 1, True) ➞ 4
    # 8 in bin: 1000, rotated 1 step to the right: 0100, in dec: 4
    
    bit_rotate(16, 1, False) ➞ 1
    # 16 in bin: 10000, rotated 1 step to the left: 00001, in dec: 1
    
    bit_rotate(17, 2, False) ➞ 6
    # 17 in bin: 10001, rotated 2 steps to the left: 00110, in dec: 6

### Notes

  * For parameters use unsigned integers only.
  * There is a solution with string operations and combined bit operations.

"""

def bit_rotate(n, m, d):
    # Get binary values (as string)
    binary = str(bin(n))[2:]
    # Get the new indexes: take into account if d = True or False
    indexes = [i%len(binary) for i in range(-len(binary)-m, 0-m)] if d else [i%len(binary) for i in range(0+m, len(binary)+m)] 
    # Make the new rotated binary value based on the indexes
    rotated = "".join([str(binary[i]) for i in indexes])
    
    return int(rotated, 2)

