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
    binary = bin(n)[2::]
    new_binary = ['0'] * len(binary)
    if not(d): # to the left
        temp = []
        for i in binary:
            temp = [ i ] + temp
        binary = temp
    for i in range(len(binary)):
        if binary[i] == "1":
            place = (i + m) % len(binary)
            new_binary[place] = "1"
    
    if not(d):
        new_binary.reverse()
​
    binary = int("".join(new_binary))
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
​
    return decimal

