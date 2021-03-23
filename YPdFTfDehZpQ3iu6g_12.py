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

def rton(r):
  l1 = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5}
  l2 = {'CM': 900, 'XC': 90, 'IX': 9, 'CD': 400, 'XL': 40, 'IV': 4}
  ans = 0
  while len(r) > 0:
    try: 
      ans += l2[r[:2]]
      r = r[2:]
    except:
      try:
        ans += l1[r[0]]
        r = r[1:]
      except: return ans + len(r)
  return ans
​
def ntor(n):
  l1 = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
  l2 = {'CM': 900, 'XC': 90, 'IX': 9, 'CD': 400, 'XL': 40, 'IV': 4}
  l1.update(l2)
  l = {k: v for v, k in l1.items()}
  ans = ''
  for i in sorted(l.keys(), reverse=True):
    while n - i >= 0:
      ans += l[i]
      n -= i
  return ans
​
def roman_numerals(arg):
  return rton(arg) if type(arg) is str else ntor(arg)

