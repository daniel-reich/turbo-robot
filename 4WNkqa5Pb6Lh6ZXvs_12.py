"""


You will be given a polynomial expression in string form. The expression will
contain any of the following operations, written using standard mathematical
notation for a single variable, "x", as illustrated in the examples below:

  * addition: x + 1
  * subtraction: x – 2
  * multiplication: 3x
  * division: x / 4
  * exponentation: x^5
  * brackets: x(x + 1)

Your task is to write a function that can evaluate such a polynomial for a
given value of x. You will receive two arguments: the polynomial string and
the input number.

If the mathematical expression contains an error, you should return
`"invalid"`.

### Examples

    evaluate_polynomial("x+1", 5) ➞ 6
    
    evaluate_polynomial("5x^2", 3) ➞ 45
    
    evaluate_polynomial("(x(x+1))/2", 4) ➞ 10
    
    evaluate_polynomial("4(x + 3))/2", 5) ➞ "invalid"
    # Invalid because parentheses not balanced.

### Notes

The string will not contain spaces.

"""

def evaluate_polynomial(poly, num):
    a = ['0','1','2','3','4','5','6','7','8','9','x','(',')','/','*','+','-','^']
    x = num
    for i in range(len(poly)):
        if poly[i] not in a:
            return 'invalid'
    if '//' in poly:
        return 'invalid'
    poly = poly.replace('^','**')
    poly = poly.replace('(','*(')
    poly = poly.replace('2x','2*x')
    poly = poly.replace('3x','3*x')
    poly = poly.replace('4x','4*x')
    poly = poly.replace('5x','5*x')
    poly = poly.replace('6x','6*x')
    poly = poly.replace('7x','7*x')
    poly = poly.replace('8x','8*x')
    poly = poly.replace('9x','9*x')
    poly = poly.replace('0x','0*x')
    poly = poly.replace('/','//')
    if len(poly) == 0:
        return 'invalid'
    return eval(poly)

