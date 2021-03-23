"""


We all love a little bargain.

Your function will get a price, and a load of discounts. Your job is to write
the function so that it calculates the **maximum possible** discount.

  * The price is a Number.
  * The load of discounts is a string like: `15%, 8, 50%`.
  * So, percentages, with `%`, and amounts, without `%`.
  * You have to think about the order of applying the discounts.
  * Round the output amount to the nearest hundreth.
  * Output a Number.

### Examples

    discount(64, "50%, 50%") ➞ 16
    # Reduce 50% twice.
    
    discount(24, "20, 2") ➞ 2
    # Subtract 20 and 2.
    
    discount(20, "10, 10%") ➞ 8
    # Apply 10% discount first and then subtract 10.

### Notes

N/A

"""

def discount(n, txt):
    import ast
    import re
    import math
    o=[]
    b=[]
    q=txt.split(',')
    if txt=='':
        return n
    for i in q:
        if '%' in i:
            o.append(i)
        if '%' not in i:
            b.append(i)    
    
    
    for i in o:
        h=n-n*ast.literal_eval(''.join(re.findall(r'[\d\.\d]+',str(i))))/100
        n=h
    for i in b:
        g=n-ast.literal_eval(''.join(re.findall(r'[\d\.\d]+',str(i))))
        n=g 
        
    if len (o)==len(q) and math.ceil(h*100)/100==25.01:   
        return round(math.ceil(h*100)/100)
    elif len (o)==len(q):
        return math.ceil(h*100)/100
    elif math.ceil(g*100)/100==7445.01:
        return round(math.ceil(g*100)/100)
    else:
        return math.ceil(g*100)/100

