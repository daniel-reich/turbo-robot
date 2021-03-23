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

L = list("IVXLCDM")
N = [1, 5, 10, 50, 100, 500, 1000]
R = dict(zip(L, N))
​
def roman_numerals(s):
  if isinstance(s, int): return num_to_roman(s)
  res = 0
  for i, x in enumerate(s):
    res += R[x] if i == len(s) - 1 or R[x] >= R[s[i + 1]] else -R[x]
  return res
​
def num_to_roman(n):
  res = ""
  while n > 0:
    l, v = next((_, x) for _, x in list(zip(L, N))[::-1] if n >= x)
    res += l
    n -= v
  return res.replace("IIII", "IV")

