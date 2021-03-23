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

def roman_to_num(r, s1):
    if len(r) == 1:
        return s1[r]
    v = 0
    for i in range(len(r) - 1):
        if s1[r[i + 1]] > s1[r[i]]:
            v -= s1[r[i]]
        else:
            v += s1[r[i]]
    return v + s1[r[len(r) - 1]]
​
​
def num_to_roman(n, s2):
    n = str(n)
    r = ''
    for i in range(len(n)):
        v = int(n[i]) * 10 ** (len(n) - 1 - i)
        if v in s2.keys():
            r += s2[v]
            l = []
        elif int(n[i]) == 4:
            l = [1 for i in range(5 - int(n[i]))] + [5]
        elif int(n[i]) < 4:
            l = [1 for i in range(int(n[i]))]
        else:
            l = [5] + [1 for i in range(int(n[i]) - 5)]
        for x in l:
            r += s2[x * 10 ** (len(n) - 1 - i)]
    return r
​
​
def roman_numerals(arg):
    s1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s2 = {v: k for k, v in s1.items()}
    if type(arg) == int:
        return num_to_roman(arg, s2)
    return roman_to_num(arg, s1)

