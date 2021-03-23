"""


Adding fractional binary numbers is similar to adding decimals. The places to
the right of the decimal point (or binary point) are halves, quarters, eighths
instead of tenths, hundredths, thousandths, etc.

Improvise a function that takes two fractional binary numbers and produces
their base-10 sum. The sum can be a whole number, a fraction, or a mixed
number. The answer should be returned as a string with fractions reduced to
lowest terms.

### Examples

    binary_sum(["1.1", "1.1"]) ➞ "3"
    # 1.5 + 1.5
    
    binary_sum(["11.1", "0.001"]) ➞ "3 5/8"
    # 3.5 + 0.125
    
    binary_sum(["1101.0", "0.0100"]) ➞ "13 1/4"
    # 13 + 1/4
    
    binary_sum(["0.11", "0.00001"]) ➞ "25/32"
    # 3/4 + 1/32
    
    binary_sum(["0.0", "101.00"]) ➞ "5"

### Notes

N/A

"""

from fractions import Fraction as Fr
def convert(binary):
    whole, decimal = binary.split(".")
    w = 1
    d = 2
    wnum = dnum = 0
    for i in whole[::-1]:
        if i == "1":
            wnum += w
        w *= 2
    for i in decimal:
        if i == "1":
            dnum += 1/d
        d *= 2
    return Fr(str(wnum + dnum))
​
def s_d(frac):
    whole = 0
    num, den = frac.numerator, frac.denominator
    while num > den:
        num -= den
        whole += 1
    return whole, num, den
​
def binary_sum(lst):
    num1 = convert(lst[0])
    num2 = convert(lst[1])
    total = num1 + num2
    if float(total).is_integer():
        return str(total)
    else:
        sd = s_d(total)
        return " ".join([str(sd[0]), str(Fr(sd[1], sd[2]))]) if sd[0] else str(Fr(sd[1], sd[2]))

