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
    nq = []
    if a % b == 0:
        return str(a/b)
    ans = str(a // b)+chr(46)
    while a!=0:
        r = a % b
        if r == 0:
            for i in nq:
                ans += str(i[1])
            break
        a = r*10
        q = a // b
        if [a, q] in nq:
            p = nq.index([a, q])
            for i in nq[:p]:
                ans += str(i[1])
            ans += chr(40)
            for i in nq[p:]:
                ans += str(i[1])
            ans += chr(41)
            break        
        else:
            nq.append([a, q])
    return ans

