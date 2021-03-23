"""


Create a function that returns the simplified version of a fraction.

### Examples

    simplify("4/6") ➞ "2/3"
    
    simplify("10/11") ➞ "10/11"
    
    simplify("100/400") ➞ "1/4"
    
    simplify("8/4") ➞ "2"

### Notes

  * A fraction is simplified if there are no common factors (except 1) between the numerator and the denominator. For example, `4/6` is **not** simplified, since `4` and `6` both share `2` as a factor.
  * If improper fractions can be transformed into integers, do so in your code (see example #4).

"""

def simplify(txt):
    temp1=""
    temp2=""
    index=txt.find('/')
    for i in range(0,index):
        temp1+=txt[i]
    for i in range(index+1,len(txt)):
        temp2+=txt[i]
    num1=int(temp1)
    num2=int(temp2)
    gcd=1
    for i in range(1,min(num1,num2)+1):
        if(num1%i==0 and num2%i==0):
            gcd=i
    if(num2//gcd==1):
        return str(num1//gcd)
    else:
        return str(num1//gcd)+'/'+str(num2//gcd)

