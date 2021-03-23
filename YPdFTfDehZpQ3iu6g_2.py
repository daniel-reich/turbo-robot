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

roman_numerals=lambda x: (roman if isinstance(x, int) else arabic)(x)
values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
numeral = {v: k for k, v in values.items()}
def roman(n):
  def digit(n, base):
    if n==10: return numeral[10*base]
    s=numerals[5*base] if n>=5 else ""
    if n%5==4: s += numeral[base] + numeral[5*base]
    else: s += numeral[base]*(n%5)
    return s
  return 'M'*(n//1000) + digit(n%1000//100,  100) + digit(n%100//10, 10) + digit(n%10, 1)
def arabic(r):
  vals = [values[c] for c in r] + [0]
  return sum(-x if x<n else x for (x, n) in zip(vals, vals[1:]))

