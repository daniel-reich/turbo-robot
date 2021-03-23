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
    if (a== 0):  
        return "0"    
    sign = -1 if (a< 0) ^ (b< 0) else 1  
    num = abs(a)  
    den = abs(b)  
    initial = num // den
    res = ""   
    if (sign == -1):  
        res += "-"
    res += str(initial)    
    if (num % den == 0):  
        return str(float(res))   
    res += "." 
    rem = num % den  
    mp = {}    
    index = 0
    repeating = False
    while (rem > 0 and not repeating) :   
        if ( rem in mp):  
            index = mp[rem]  
            repeating = True
            break          
        else: 
            mp[rem] = len(res)  
        rem = rem * 10
        temp = rem // den  
        res += str(temp ) 
        rem = rem % den  
    if (repeating) :  
        res += ")"
        x = res[:index] 
        x += "("
        x += res[index:] 
        res = x
    return res

