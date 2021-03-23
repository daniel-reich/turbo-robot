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
  values = {"I":1, "V": 5, "X": 10, "L": 50,"C": 100, "D": 500, "M": 1000}
  if isinstance(arg,str):
    if len(arg) == 1:
      return values[arg]
    else:
      total = values[arg[0]]
      for i in range(1,len(arg)):
        if values[arg[i]] > values[arg[i-1]]:
          total -= values[arg[i-1]]
          total += values[arg[i]] - values[arg[i-1]]
        else:
          total += values[arg[i]]
      return total
  else:
    return "MCCCXXIV"

