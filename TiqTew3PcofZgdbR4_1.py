"""


A decimal number can be represented as a sequence of bits. To illustrate:

    6 = 00000110
    23 = 00010111

From the bitwise representation of numbers, we can calculate the **bitwise
AND** , **bitwise OR** and **bitwise XOR**. Using the example above:

    bitwise_and(6, 23) ➞ 00000110
    
    bitwise_or(6, 23) ➞ 00010111
    
    bitwise_xor(6, 23) ➞ 00010001

Write three functions to calculate the **bitwise AND** , **bitwise OR** and
**bitwise XOR** of two numbers.

### Examples

    bitwise_and(7, 12) ➞ 4
    
    bitwise_or(7, 12) ➞ 15
    
    bitwise_xor(7, 12) ➞ 11

### Notes

N/A

"""

for s in["and&","or |","xor^"]:exec("bitwise_"+s[:3]+"=lambda a,b:a"+s[3]+"b")

