"""


Create a function that takes an amount of monetary change (e.g. 47 cents) and
breaks down the most efficient way that change can be made using USD quarters,
dimes, nickels and pennies. Your function should return a dictionary.

### Examples

    make_change(47) ➞ { "q": 1, "d": 2, "n": 0, "p": 2 }
    
    make_change(24) ➞ { "q": 0, "d": 2, "n": 0, "p": 4 }
    
    make_change(92) ➞ { "q": 3, "d": 1, "n": 1, "p": 2 }

### Notes

Amount given will always be less than 100 and more than 0.

"""

def make_change(c):
    a=c//25
    b=c-a*25
    d=b//10
    e=b-d*10
    f=e//5
    g=e-f*5
    h={}
    h["q"]=a
    h["d"]=d
    h["n"]=f
    h["p"]=g
    return h

