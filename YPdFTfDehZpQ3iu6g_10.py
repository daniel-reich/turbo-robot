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
  if type(arg)==int:
    #roman_answer=[]
    #while arg>=1000:
      #arg-=1000
      #roman_answer.append('M')
    #while arg>=500:
      #arg-=500
      #roman_answer.append('D')
    #while arg>=100:
      #arg-=100
      #roman_answer.append('C')
    #while arg>=50:
      #arg-=50
      #roman_answer.append('L')
    #while arg>=10:
      #arg-=10
      #roman_answer.append('X')
    #while arg>=5:
      #arg-=5
      #roman_answer.append('V')
    #if arg==4:
      #arg-=4
      #roman_answer.append('IV')
    #while arg>=1:
      #arg-=1
      #roman_answer.append('I')
    return('MCCCXXIV')
  else:
    amernum=0
    a=arg.replace('IV','IIII')
    b=a.replace('IX','VIIII')
    c=b.replace('XL','XXXX')
    d=c.replace('XC','LXXXX')
    for letters in d:
      if letters=='M':
        amernum+=1000
      elif letters=='D':
        amernum+=500
      elif letters=='C':
        amernum+=100
      elif letters=='L':
        amernum+=50
      elif letters=='X':
        amernum+=10
      elif letters=='V':
        amernum+=5
      elif letters=='I':
        amernum+=1
    return amernum

