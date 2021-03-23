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
  rom2num = dict(zip('IVXLCDM',[1,5,10,50,100,500,1000]))
  num2rom = [(v,k) for k,v in rom2num.items()] + [(4,'IV'),(9,'IX'),(40,'XL'),(90,'XC'),(400,'CD'),(900,'CM')]
  if type(arg) == str:
    res = 0
    for i,c in enumerate(arg):
      if i < len(arg)-1 and rom2num[c] < rom2num[arg[i+1]]:
        res -= rom2num[c]
      else:
        res += rom2num[c]
  else:
    res = ''
    for num,rom in sorted(num2rom)[::-1]:
      i,arg = divmod(arg,num)
      res += rom*i
  return res

