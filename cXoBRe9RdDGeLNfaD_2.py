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
    sep = ' + ' if ' + 'in exp else ' - '
    n1, n2 = [eval(x) for x in exp.split(sep)]
    ans = eval(exp)
    if any(-128 > x or x > 127 for x in [n1, n2, ans]):
        return 'Overflow'
    return ans, '{}{}{} = {}'.format(to_binr(n1), sep, to_binr(n2), to_binr(ans))
​
def to_bin(n):
    ans = []
    while n > 0:
        ans.append(n % 2)
        n //= 2
    return ''.join(str(b) for b in ans[::-1]) if ans else '0'
​
def to_binr(n):
    return to_bin(n) if n >= 0 else to_bin(256+n)

