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
    convertRomNum = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1, '0': 0}
    convertNumRom = ({'borrow': 'X', 'base': 'V', 'add': 'I'},
                     {'borrow': 'C', 'base': 'L', 'add': 'X'},
                     {'borrow': 'M', 'base': 'D', 'add': 'C'})
​
    if type(arg) == str:
        rom = arg
        rom += '0'
        numList = []
        for i in range(len(rom) - 1):
            if convertRomNum[rom[i]] < convertRomNum[rom[i + 1]]:
                numList.append(convertRomNum[rom[i]] * - 1)
            else:
                numList.append(convertRomNum[rom[i]])
                
        return sum(numList)
​
    if type(arg) == int:
        num = str(arg)[::-1]
        romString = ''
        for i in range(3):
            if i == len(num):
                break
            if num[i] == '9':
                romString += convertNumRom[i]['borrow'] + convertNumRom[i]['add']
            elif 9 > int(num[i]) > 4:
                for j in range(int(num[i]) - 5):
                    romString += convertNumRom[i]['add']
                romString += convertNumRom[i]['base']
            elif num[i] == '4':
                romString += convertNumRom[i]['base'] + convertNumRom[i]['add']
            else:
                for j in range(int(num[i])):
                    romString += convertNumRom[i]['add'] 
        
        return int(num[3:]) * 'M' + romString[::-1] if len(num) > 3 else romString[::-1]

