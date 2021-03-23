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

POWERS = {(base, power): base**power for base in range(1, 51) for power in range(200)}
​
def to_base(d, to_base, values):
    # convert decimal integer (base 10) to base to_base
    res = []
    for p in range(50, -1, -1):
        power = POWERS[(to_base, p)]
        m = d // power
        res.append(str(values[m]))
        d = d % power
    while res[0] == str(values[0]):
        res.pop(0)
    return ''.join(res)
​
def base_n(base, values, num):
    if len(values) != base:
        return False
    return to_base(num, base, values)

