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

def base_conv(n, b):
    base_str = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    rest = []
    result = ''
​
    if isinstance(n, int):
​
        while n // b > 0:
            rest.append(n % b)
            n = n // b
        rest.append(n % b)
​
        for item in rest:
            result += base_str[item]
​
        return result[::-1]
​
    for letter in n:
        if letter not in base_str[:b]:
            return str(n) + ' is not a base ' + str(b) + ' number.'
​
    rest = [base_str.index(letter) for letter in n[::-1]]
    return sum([item * (b ** index) for index, item in enumerate(rest)])

