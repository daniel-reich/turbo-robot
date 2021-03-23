"""


Create a function that will take either a **string** containing a roman
numeral, or an **integer**.

  1. Given a string, return the integer value of that roman numeral.
  2. Given an integer, return the equivalent roman numeral.

### Symbols to Values

    I ➞ 1
    
    V ➞ 5
    
    X ➞ 10
    
    L ➞ 50
    
    C ➞ 100
    
    D ➞ 500
    
    M ➞ 1000

### Examples

    roman_numerals("V") ➞ 5
    
    roman_numerals("IV") ➞ 4
    
    roman_numerals("CII") ➞ 102
    
    roman_numerals(45) ➞ "XLV"
    
    roman_numerals(1666) ➞ "MDCLXVI"

### Notes

Numerical and Roman Numeral inputs will be positive numbers between 1 and
9999.

"""

d = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), 
     (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), 
     (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
​
def roman_numerals(arg): 
    if isinstance(arg, int):
        res, n = '', int(arg)
        for value, numeral in d:
            res += numeral * (n//value)
            n %= value       
    else:
        res = 0
        while arg:
            for value, numeral in sorted(d, key=lambda x: -len(x[1])):
                if numeral in arg:
                    res += value
                    arg = arg.replace(numeral, '', 1)
    return res

