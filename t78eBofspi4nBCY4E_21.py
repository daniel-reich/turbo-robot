"""


Create a function that allows you to convert from a positive base 10 integer
to any other base from 2 to 26, and also does the reverse, converts from base
2 to 26 back to base 10. The digits in the new base will be the lower case
letters a-z with a=0 and z=25. If the number is out of range for the base
specified, return the error message shown in the examples.

### Examples

    base_conv(15, 2) ➞ "bbbb"
    # 1111
    
    base_conv(16, 2) ➞ "baaaa"
    # converts 16 (base 10) to base 2
    
    base_conv(1234, 10) ➞ "bcde"
    
    base_conv("bac", 3) ➞ 11
    # converts "bac" (base 3) to base 10
    # 1*3**2 + 0*3 + 2 = 11
    
    base_conv("dac", 3) ➞ "dac is not a base 3 number."

### Notes

N/A

"""

def base_convert(num, base_num):
    if num < base_num:
        return [num]
    i = 0
    while base_num ** i < num:
        i += 1
    if num == base_num ** i:
        base_digit = i
        result = [0 for _ in range(i + 1)]
    else:
        base_digit = i - 1
        result = [0 for _ in range(i)]
    for k in range(i):
        if (num // base_num ** base_digit) == 0:
            result[k] = 0
        elif num // base_num ** (base_digit) > 0 and num % base_num ** (base_digit) == 0:
            result[k] = (num // base_num ** (base_digit))
        elif num // base_num ** (base_digit) > 0 and num % base_num ** (base_digit) != 0:
            result[k] = (num // base_num ** (base_digit))
        num -= (num // base_num ** (base_digit)) * (base_num ** (base_digit))
        base_digit -= 1
    return result
def base_conv(n, b):
    if type(n) == int:
       result_base = base_convert(n, b)
       result = ""
       for num in result_base:
           result += chr(num + ord("a"))
    elif type(n) == str:
        result = 0
        for i in range(len(n)):
            if 0 <= (ord(n[i]) - ord("a")) < b:
                result += (ord(n[i]) - ord("a")) * (b ** (len(n) - i -1))
            else:
                return "{} is not a base {} number.".format(n, b)
​
    return result

