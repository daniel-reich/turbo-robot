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

def bitwise_and(n1, n2):
  n1 = list(bin(n1))[2:]
  n2 = list(bin(n2))[2:]
  while len(n1) < len(n2):
    n1.insert(0, "0")
  while len(n2) < len(n1):
    n2.insert(0, "0")
  return int("".join(["1" if n1[i] == "1" and n2[i] == "1" else "0" for i in range(len(n1))]), 2)
​
def bitwise_or(n1, n2):
  n1 = list(bin(n1))[2:]
  n2 = list(bin(n2))[2:]
  while len(n1) < len(n2):
    n1.insert(0, "0")
  while len(n2) < len(n1):
    n2.insert(0, "0")
  return int("".join(["1" if n1[i] == "1" or n2[i] == "1" else "0" for i in range(len(n1))]), 2)
​
def bitwise_xor(n1, n2):
  n1 = list(bin(n1))[2:]
  n2 = list(bin(n2))[2:]
  while len(n1) < len(n2):
    n1.insert(0, "0")
  while len(n2) < len(n1):
    n2.insert(0, "0")
  return int("".join(["1" if (n1[i] == "1" or n2[i] == "1") and n1[i] != n2[i] else "0" for i in range(len(n1))]), 2)

