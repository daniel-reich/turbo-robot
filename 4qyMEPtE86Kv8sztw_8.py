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

def binary_sum(nums):
    def base10(n):
        a = n.split(".") [0][::-1]
        b = n.split(".") [1]
​
        b10 = 0
​
        d = 1
​
        for x in range(len(b)):
            d *= 2
            if b [x] == "1":                   
                b10 += 1/d
​
        d = 0
​
        for x in range(len(a)):
            if a [x] == "1":
                b10 += 2**d
            d += 1
​
        return b10
​
    n1 = base10(nums [0])
    n2 = base10(nums [1])
​
    sum = float(n1) + float(n2)
​
    i = str(sum).split(".")[0]
    d = str(sum).split(".")[1]
​
    if i == "0":
        i = ""
    elif not d == "0":
        i += " "
​
    if not d == "0":
        top = int(d)
        bot = 10**len(d)
​
        for x in reversed(range(top+1)):
            if bot % x == 0 and top % x == 0:
                bot /= x
                top /= x
                break
​
        fra = str(int(top)) + "/" + str(int(bot))
​
        i += fra
​
    if i == "":
        i = "0"
​
    return i

