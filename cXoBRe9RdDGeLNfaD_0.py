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

def eight_bit(exp):
    r=range(-128,128)
    res=eval(exp)
    exl=exp.split()
    if res in r and int(exl[0]) in r and int(exl[2]) in r:
        b1=bin(int(exl[0]) & 255)[2:]
        b2=bin(int(exl[2]) & 255)[2:]
        bres=bin(res & 255)[2:]
        return (res,'{} {} {} = {}'.format(b1,exl[1],b2,bres))
    return 'Overflow'

