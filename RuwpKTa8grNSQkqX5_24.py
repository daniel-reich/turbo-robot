"""


Performing division on a fraction often results in an infinitely repeating
decimal.

    1/3=.3333333...  1/7=.142857142857...

Create a function that takes a decimal in string form with the repeating part
in parentheses and returns the equivalent fraction in string form and in
lowest terms.

### Examples

    fractions("0.(6)") ➞ "2/3"
    
    fractions("1.(1)") ➞ "10/9"
    
    fractions("3.(142857)") ➞ "22/7"
    
    fractions("0.19(2367)") ➞ "5343/27775"
    
    fractions("0.1097(3)") ➞ "823/7500"

### Notes

N/A

"""

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def fractions(n):
    r=n.find(".")
    g=n.find("(")
    h=n.find(")")
    w=int(n[:r])
    if r+1!=g:
        a=n[r+1:g]
        b=n[g+1:h]
        c=int(a+b)
        s=[c-int(a),(10**(h-g-1)-1)*10**(g-r-1)]
        q=gcd(s[0],s[1])
        x,y=[s[0]//q,s[1]//q]
        return "{}/{}".format(w*y+x,y) 
    else :
        s=[int(n[g+1:h]),(10**(h-g-1)-1)]
        q=gcd(s[0],s[1])
        s1=[s[0]//q,s[1]//q]
        return "{}/{}".format(w*s1[1]+s1[0],s1[1])

