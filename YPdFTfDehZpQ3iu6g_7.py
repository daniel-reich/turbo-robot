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

keys = {"I":1, "V":5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
keys2 = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
replacements = {"IV":"IIII","IX":"VIIII","XL": "XXXX", "XC": "LXXXX", "CD":"CCCC", "CM":"DCCCC"}
def char(k,n):
  return keys2[pow(10,k)] * n if n < 4 else "IV" if n == 4 else keys2[5 * pow(10,k)] + keys2[pow(10,k)] * n % 5 
  
def roman_numerals(arg):
  if isinstance(arg,str):
    for el in replacements.keys():
      arg = arg.replace(el,replacements[el])
    return sum(list(map(lambda x: keys[x],arg)))
  else:
    chars = list(map(lambda x: char(len(str(arg))-x-1,int(str(arg)[x])),range(0,len(str(arg)))))
    string = ''.join(chars)
    string = string.replace("IIII","IV")
    return string

