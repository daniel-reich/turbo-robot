"""


You are given a `base` (int), a list of `values` (list), and a `num` (int) to
be converted.

You are to use the values to translate the number into the base. Return
`False` if there aren't enough/too little values in the value list (it should
have the same length as the `base`). The values in value list starts with
elements representing values from zero to base - 1. Return the converted
number in string type.

### Examples

    base_n(10, [0, 1, 3, 2, 4, 5, 6, 7, 8, 9], 32) ➞ "23"
    
    base_n(8, ["zero", "one", "two", "three", "four", "five", "six", "seven"], 128 ) ➞ "twozerozero"
    
    base_n(2, [1, 0], 8) ➞ "0111"
    
    base_n(10, list("q*CYj#r-3a"), 1234567890) ➞ "*CYj#r-3aq"

### Notes

The number to be translated is always in BASE-10, non-negative and an integer.

"""

def base_convert(num, base_num):
    if num < base_num:
        return [num]
    i = 0
    while base_num ** i < num:
        i += 1
    if num == base_num ** i:
        base_digit = i
        result = [0 for _ in range(i+1)]
    else:
        base_digit = i -1
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
​
def base_n(base, values, num):
    if len(values) != base:
        return False
    result_base = base_convert(num, base)
    result = ""
    for num in result_base:
        result += str(values[num])
    return result

