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

def gcf(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcf(b,a%b) 
 
def mixed_number(Input):
    top = ''
    if Input[0]=="-":
        pos = "-"
    else:
        pos = ""
​
    for i in Input:
        if i == '/':
            break
        top+=i
    bottom = ''
    for i in Input[len(top)+1:]:
        if i == '/':
            break
        bottom+=i
        
    bottom = int(bottom)
    top = abs(int(top))
    if top//bottom == top/bottom:
        return pos + str(top//bottom) 
    else:
        Gcf = gcf(top,bottom)
        if str(top//bottom) == "0":
                return pos +str(int((top/Gcf)%(bottom/Gcf)))+"/" + str(int(bottom/Gcf))
        return pos + str(top//bottom) + ' ' + str(int((top/Gcf)%(bottom/Gcf)))+"/" + str(int(bottom/Gcf))

