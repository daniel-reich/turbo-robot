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

def binary_num_convert(num):
    num_lst = num.split(".")
    total_1 = 0
    total_2 = 0
    for i in range(len(num_lst[0])):
        total_1 += int(num_lst[0][i]) * ( 2 ** (len(num_lst[0]) - 1 - i))
    for i in range(len(num_lst[1])):
        total_2 += float(int(num_lst[1][i]) * (1/ (2 ** (i +1))))
    return total_1 + total_2
​
def decimal_convert(num):
    i = 0
    while int(num * (2 ** i)) != num * ( 2** i):
        i += 1
    return str(int(num * (2 ** i))) + "/" + str(2 ** i)
​
​
def binary_sum(lst):
    total = 0
    for num in lst:
        total += binary_num_convert(num)
    if int(total) == total:
        return str(int(total))
    elif total < 1:
        return str(decimal_convert(total))
    elif total >=1:
        return str(int(total)) + " " + decimal_convert(total-int(total))

