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
    numlist = [1000,500,100,50,10,5,1]
    romanlist = ['M', 'D', 'C', 'L','X','V','I']
    IntToRoman = {'I': 1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if isinstance(arg,int):
        romandata = ''
        for i in range(len(numlist)):
            if numlist[i] == 1000 or numlist[i] == 100 or numlist[i] == 10 or numlist[i] == 1:
                while (arg // numlist[i] != 0):
                    if arg // numlist[i] <= 3:
                        romandata += romanlist[i]
                        arg -= numlist[i]
                    elif arg // numlist[i] == 4:
                        romandata += romanlist[i] + romanlist[i - 1]
                        arg -= numlist[i] * 4
                    elif arg // numlist[i] == 5:
                        romandata += romanlist[i - 1]
                        arg -= numlist[i] * 5
                    elif arg // numlist[i] > 5 and arg // numlist[i] <= 8:
                        romandata += romanlist[i - 1] + romanlist[i] * (arg // numlist[i] - 5)
                        arg -= numlist[i] * (arg // numlist[i])
                    elif arg // numlist[i] == 9:
                        romandata += romanlist[i] + romanlist[i - 2]
                        arg -= numlist[i] * (arg // numlist[i])
        return romandata
    else:
        intnum = 0
        for i in range(1,len(arg)):
            last = arg[i-1]
            next = arg[i]
​
            if IntToRoman[last] < IntToRoman[next]:
                intnum -= IntToRoman[last]
            else :
                intnum += IntToRoman[last]
        intnum += IntToRoman[arg[len(arg)-1]]
        return intnum

