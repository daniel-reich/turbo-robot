"""


Declare a `division()` function that gets two natural numbers (`a`, `b`) and
return a string containing the rational number `a` / `b` in the form of a
decimal fraction, possibly **periodic**.

### Examples

    division(2, 5) ➞ "0.4"
    
    division(1, 6) ➞ "0.1(6)"
    
    division(1, 3) ➞ "0.(3)"
    
    division(1, 7) ➞ "0.(142857)"
    
    division(1, 77) ➞ "0.(012987)"

### Notes

  * The length of a periodic fraction can be more than **20 numbers**.
  * The function should be efficient.

"""

def division(a, b):
    res = [a // b]
    rem = [a % b, a % b]
    period_start = -1
​
    while period_start < 0 < rem[-1]:
        rem[-1] *= 10
        res.append(rem[-1] // b)
        remainder = rem[-1] % b
        if remainder * 10 in rem:
            period_start = rem.index(remainder * 10)
        else:
            rem.append(remainder)
​
    if period_start > 0:
        str_res = '{}.{}({})'.format(res[0], ''.join(str(i) for i in
                                                     res[1: period_start]),
                                     ''.join(str(i) for i in
                                             res[period_start:]))
    else:
        pre_period = ''.join(str(i) for i in res[1:])
        str_res = '{}.{}'.format(res[0], pre_period if pre_period else '0')
    return str_res

