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
    i = str(a//b)
    r = a % b
    rems = []
    dec = ''
    while r and r not in rems:
        rems.append(r)
        dec += str(10*r//b)
        r = (10*r) % b
    if not dec: dec='0'
    if r == 0:
        return "{}.{}".format(i,dec)
    idx = rems.index(r)
    return "{}.{}({})".format(i,dec[:idx],dec[idx:])

