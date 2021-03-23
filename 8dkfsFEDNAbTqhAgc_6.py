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
    lst = []
    s = ""
    y = 1
​
    while y != 0:
        x, y = divmod(a, b)
        add = (x, y)
        
        if add not in lst:
            lst.append(add)
        else:
            start = (lst.index(add))
            start += len(str(lst[0][0])) - 1
            s = s[ : start] + "(" + s[start : ] + ")"
            break
        
        s += str(x)
        if x == 0:
            a *= 10
            if "." not in s:
                lst.append(".")
                s +="."
        if x > 0:
            a = 10 * y
            if "." not in s:
                lst.append(".")
                s +="."
    if s[-1] == ".":
        s += "0"
    return s

