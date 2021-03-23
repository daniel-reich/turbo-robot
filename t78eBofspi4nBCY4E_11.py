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

VALUES = {chr(97+i): i for i in range(26)}
INV_VALUES = {value: key for key, value in VALUES.items()}
​
POWERS = {(base, power): base**power for base in range(1, 37) for power in range(200)}
​
def from_base(k, base_k):
    # convert integer k in base base_k to decimal (base 10)
    L = len(k)
    res = 0
    for i in range(L - 1, -1, -1):
        res += VALUES[k[i]] * POWERS[(base_k, L - 1 - i)]
    return res
​
def to_base(d, to_base):
    # convert decimal integer (base 10) to base base_k
    res = ""
    for p in range(50, -1, -1):
        power = POWERS[(to_base, p)]
        m = d // power
        res += INV_VALUES[m]
        d = d % power
    while res[0] == 'a':
        res = res[1:]
    return res
​
def base_conv(n,b):
    if type(n) == int:
        ans = to_base(n, b)
        return ans
    L = [ord(c) - 97 for c in n]
    if min(L) < 0 or max(L) >= b:
        return n + " is not a base " + str(b) + " number."
    ans = from_base(n, b)
    return ans

