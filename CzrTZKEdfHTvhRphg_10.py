"""


Create a function that takes a string representing a fraction, and return a
string representing that input as a mixed number.

  * Mixed numbers are of the form `1 2/3` — note the space between the whole number portion and the fraction portion.
  * Resulting fractions should be fully reduced (see example #2).
  * If a result is a whole number with no fractional remainder, return only the whole number portion (see example #3).
  * If a result is only fractional with no whole number, return only the fractional portion (see example #4).
  * If a result is negative, the whole number should carry the negative sign. If the result would not have a whole number portion, the numerator of the fractional portion should carry the negative sign (see examples #5 - #7).

### Examples

    mixed_number("5/4") ➞ "1 1/4"
    
    mixed_number("6/4") ➞ "1 1/2"
    
    mixed_number("8/4") ➞ "2"
    
    mixed_number("4/6") ➞ "2/3"
    
    mixed_number("-1/4") ➞ "-1/4"
    
    mixed_number("-5/4") ➞ "-1 1/4"
    
    mixed_number("-8/4") ➞ "-2"

### Notes

All provided inputs will be formatted similarly, negative numbers will be
provided in the numerator portion only, and all inputs will contain no spaces,
invalid characters, or zero denominators.

"""

def mixed_number(frac): 
    bruch = list(frac)
    length = len(bruch)
    n = 0
    num1 = ""
    num2 = ""
    nummer = ''
    negativ = ''
    while n < length: #get both numbers
        char = bruch[n]
        if char == '-':
            negativ = char
        elif 47 < ord(char) < 58:
            nummer += char
        else:
            num1 = nummer
            nummer = ''
        n += 1
    num2 = nummer
    num1 = int(num1) #string to int
    num2 = int(num2) #string to int
    
    if (num1 / num2) > 1: #vereinfachen
        zaehler = (num1 % num2)
        zahl = (num1-zaehler)/num2
    else:
        zaehler = num1
        zahl = 0
    
    nenner = num2
    
    if zaehler == 0:
        return(negativ+str(round(zahl)))
    else:
        n = (zaehler)
        while  n > 0:
            if zaehler%n == 0 and nenner%n == 0:
                zaehler = zaehler/n
                nenner = nenner/n
                n = n-1
            else:
                n = n-1
        if zahl == 0:
            string = ''
            string = negativ+str(round(zaehler))+'/'+str(round(nenner))
            return(string)
        else:
            string = ''
            string = negativ+str(round(zahl))+' '+str(round(zaehler))+'/'+str(round(nenner))
            return(string)

