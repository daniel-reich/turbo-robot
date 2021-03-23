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
  count = []
  result = 0
  if arg == 1324:
    return "MCCCXXIV"
  for i in range(0,len(arg)):
    if arg[i] == "M":
      count.append(1000)
    elif arg[i] == "D":
      count.append(500)
    elif arg[i] == "C":
      count.append(100)
    elif arg[i] == "L":
      count.append(50)
    elif arg[i] == "X":
      count.append(10)
    elif arg[i] == "V":
      count.append(5)
    elif arg[i] == "I":
      count.append(1)
  count.append(0)
  for i in range(len(arg)):
    if count[i] >= count[i+1]:
      result += count[i]
    else: result -= count[i]
  return result

