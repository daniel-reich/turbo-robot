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
  if isinstance(arg,str):
    arg = [letter for letter in arg]
    n = 0
    try:
      if len(arg) > 1 and arg[0] == 'C' and arg[1] == 'M':
        n-= 100
        arg.pop(0)
      while arg[0] == 'M':
        n += 1000
        arg.pop(0)
​
      if len(arg) > 1 and arg[0] == 'C' and arg[1] == 'D':
        n-= 100
        arg.pop(0)
      while arg[0] == 'D':
        n += 500
        arg.pop(0)
​
      if len(arg) > 1 and arg[0] == 'X' and arg[1] == 'C':
        n-= 10
        arg.pop(0)
      while arg[0] == 'C':
        n += 100
        arg.pop(0)
​
      if len(arg) > 1 and arg[0] == 'X' and arg[1] == 'L':
        n-= 10
        arg.pop(0)
      while arg[0] == 'L':
        n += 50
        arg.pop(0)
​
      if len(arg) > 1 and arg[0] == 'I' and arg[1] == 'X':
        n-= 1
        arg.pop(0)
      while arg[0] == 'X':
        n += 10
        arg.pop(0)
​
      if len(arg) > 1 and arg[0] == 'I' and arg[1] == 'V':
        n -= 1
        arg.pop(0)
      while arg[0] == 'V':
        n += 5
        arg.pop(0)
      n += arg.count('I')
    except:
      return n
    return n
  else:
    res = ''
    if arg%1000 >= 900:
      res += 'CM'
      arg -= 900
    while arg >= 1000:
      res += 'M'
      arg -= 1000
    if arg >= 500:
      res += 'D'
      arg -= 500
    if arg % 100 >= 90:
      res += 'XC'
      arg -= 90
    while arg >= 100:
      res += 'C'
      arg -= 100
    if arg >= 50:
      res += 'L'
      arg -= 50
    if arg % 10 == 9:
      res += 'IX'
      arg -= 9
    while arg >= 10:
      res += 'X'
      arg -= 10
    if arg >= 5:
      res += 'V'
      arg -= 5
    if arg == 4:
      res += 'IV'
      arg -= 4
    while arg:
      res += 'I'
      arg -= 1
    return res

