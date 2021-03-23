"""


Given a _string_ containing an _algebraic equation_ , calculate and **return
the value of x**. You'll only be given equations for simple **addition** and
**subtraction**.

### Examples

    eval_algebra("2 + x = 19") ➞ 17
    
    eval_algebra("4 - x = 1") ➞ 3
    
    eval_algebra("23 + 1 = x") ➞ 24

### Notes

  * There are spaces between every number and symbol in the string.
  * x may be a negative number.

"""

def eval_algebra(eq):
    eql= (eq.replace(" ","")).split('=')
    if ("x" in eql[0]):
        if ("+" in eql[0]):
            newl=eql[0].split("+")
            
            return int(eql[1])-int(newl[1]) if newl[0].isalpha() else int(eql[1])-int(newl[0])
        else:
            newl=eql[0].split("-")
            if eql[0].count("-")==2:
                #x is second
                return -int(eql[1])-int(newl[1])
            else:
                return int(eql[1])+int(newl[1]) if "x" in newl[0] else -int(eql[1])+int(newl[0])
    else:
        return eval(eql[0])

