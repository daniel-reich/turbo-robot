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
  d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
  if type(arg) == type('a'):
    i = 0
    chrs = list(arg)
    if len(chrs) > 1:
      for j in range(len(chrs)-1):
        if d[chrs[j]] >= d[chrs[j+1]]:
          i += d[chrs[j]]
        else:
          i -= d[chrs[j]]
    i += d[chrs[-1]]
    return i
  else:
    d = {'1':'I', '2':'II', '3':'III', '4':'IV', '5':'V', '6':'VI', '7':'VII', '8':'VIII', '9':'IX'}
    digs = str(arg)
    s = int(digs[0])*'M' + int(digs[1])*'C' + int(digs[2])*'X' + d[digs[-1]]
    return s

