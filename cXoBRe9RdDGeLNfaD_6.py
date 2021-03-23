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
    num_one, operator, num_two = exp.split(" ")
    num_one, num_two = int(num_one), int(num_two)
    if num_one < -128 or num_one > 127 or num_two < -128 or num_two > 127:
        return "Overflow"
    result = eval("{}{}{}".format(num_one, operator, num_two))
    if result > 127 or result < -128:
        return "Overflow"
    return (result, "{} {} {} = {}".format(bin(num_one)[2:] if num_one > 0 else bin(num_one & 255)[2:], operator, bin(num_two)[2:] if num_two > 0 else bin(num_two & 255)[2:], bin(result & 255)[2:]))

