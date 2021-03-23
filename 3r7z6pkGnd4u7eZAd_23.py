"""


Given a list of _math equations_ (given as strings), return the **percentage
of correct answers** _as a string_. Round to the nearest _whole number_.

### Examples

    mark_maths(["2+2=4", "3+2=5", "10-3=3", "5+5=10"]) ➞ "75%"
    
    mark_maths(["1-2=-2"]), "0%"
    
    mark_maths(["2+3=5", "4+4=9", "3-1=2"]) ➞ "67%"

### Notes

  * You can expect only _addition_ and _subtraction_.
  * Note how there aren't any spaces in any given equation.

"""

def mark_maths(lst):
    fl=[]
    for el in lst:
        for i in range(len(el)):
            if (el[i]=='+') | (el[i]=='-'):
                oi=i
            if el[i]=='=':
                 ei=i
                 a=int(el[:oi])
                 b=int(el[oi+1:ei])
                 r=int(el[ei+1:])
                 if el[oi]=='+':
                        c=a+b
                        if c==r:
                            fl.append(1)
                        else:
                            fl.append(0)
                 if el[oi]=='-':
                    c=a-b
                    if c==r:
                        fl.append(1)
                    else:
                        fl.append(0)
    fls=str(round((sum(fl)*100)/len(fl),0))
    return fls.split('.')[0]+'%'

