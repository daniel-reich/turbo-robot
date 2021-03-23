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

def roman_numerals(arg):
  key = (('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1))
  dic = dict(key)
  if type(arg) is str:
    res = 0
    last = 0
    for i in arg:
      res += dic[i] - (last * 2 * (last and last < dic[i]))
      last = dic[i]
    return res
  else:
    res = ''
    for rom, dec in key:
      res += rom * (arg//dec)
      arg %= dec
    for un, fv, tn in (('I', 'V', 'X'), ('X', 'L', 'C'), ('C', 'D', 'M')):
      res = res.replace(fv + un*4, un+tn).replace(un*4, un+fv)
    return res

