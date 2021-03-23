"""


You will be given a simple string expression representing an addition or
subtraction in 8-bit 2's complement arithmetic. Write a function that returns
the result in base 10 followed by a binary representation. If any of the
values are outside the range of 8-bit 2's complement, return `"Overflow"`.

### Examples

    eight_bit("3 + 12") ➞ (15, "11 + 1100 = 1111")
    
    eight_bit("3 - 12") ➞ (-9, "11 - 1100 = 11110111")
    
    eight_bit(-18 - 6) ➞ (-24, "11101110 - 110 = 11101000")
    
    eight_bit(65 + 70) ➞ "Overflow"
    
    eight_bit(-127 + 127) ➞ (0, "10000001 + 1111111 = 0")

### Notes

Numbers in 8-bit 2's complement notation can range from -128 to 127. The
eighth (leftmost) bit signifies a negative number. See **Resources** for
details.

"""

def to_two_complement(n):
    b = bin(abs(n))[2:]
    if n >= 0:
        return b
    b = b.zfill(8)
    c = ""
    for bit in b:
        c += '1' if bit == '0' else '0'
    return bin(int("0b" + c, 2) + 1)[2:]
    
def eight_bit(exp):
    a, op, b = exp.split()
    if not (-128 <= int(a) <= 127 and -128 <= int(b) <= 127):
        return 'Overflow'
    ba = to_two_complement(int(a))
    bb = to_two_complement(int(b))
    if op == '+':
        # addition
        c = int(a) + int(b)
        if c > 127:
            return 'Overflow'
        bc = to_two_complement(int(c))
        return (c, ba + " + " + bb + " = " + bc)
    # subtraction
    c = int(a) - int(b)
    if c < -128:
        return 'Overflow'
    bc = to_two_complement(int(c))
    return (c, ba + " - " + bb + " = " + bc)

