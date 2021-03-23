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

def division(n, d):
    units, n = divmod(n, d) 
    rem_dict = { n: 0}
    decimals = []
    while n > 0:
        dec, n = divmod(n * 10, d)
        decimals.append(dec)
        if n in rem_dict:
            return str(units) + '.' + ''.join(map(str, decimals[:rem_dict[n]])) + '(' + ''.join(map(str, decimals[rem_dict[n]:])) + ')'
        else:
            rem_dict[n] = len(decimals)
    return str(units) + '.' + (''.join(map(str, decimals)) if len(decimals) > 0 else '0')

